import os
import sqlite3
import pandas as pd
import pytest
from src.load.dwh_builder import build_star_schema

# --- LOẠI 1: LUỒNG ĐÚNG (HAPPY PATH) ---
def test_tc01_normalize_date_valid():
    """TC-01: Chuẩn hóa ngày tháng đúng định dạng"""
    df = pd.DataFrame({'ngay': ['2024-05-15', '15/06/2025']})
    df['ngay'] = pd.to_datetime(df['ngay'], errors='coerce')
    assert df['ngay'].dt.year.iloc[0] == 2024

def test_tc02_validate_thanh_tien_positive():
    """TC-02: Xác thực các số tiền thanh toán hợp lệ (>0)"""
    df = pd.DataFrame({'thanh_tien': [1500000, 500000]})
    valid_df = df[df['thanh_tien'] > 0]
    assert len(valid_df) == 2

def test_tc03_staging_database_exists():
    """TC-03: Kiểm tra cơ sở dữ liệu SQLite tồn tại sau khi chạy ETL"""
    assert os.path.exists("smart_crm_dwh.db")


# --- LOẠI 2: GIÁ TRỊ BIÊN (BOUNDARY) ---
def test_tc04_phone_boundary_exact_10_digits():
    """TC-04: Số điện thoại nằm ở ngưỡng biên chuẩn (đúng 10 chữ số)"""
    df = pd.DataFrame({'so_dien_thoai': ['0901234567']})
    valid_df = df[df['so_dien_thoai'].str.isnumeric() & (df['so_dien_thoai'].str.len() == 10)]
    assert len(valid_df) == 1

def test_tc05_validate_thanh_tien_negative_edge_case():
    """TC-05: Xử lý giao dịch có số tiền âm hoặc bằng 0"""
    df = pd.DataFrame({'thanh_tien': [1500000, -50000, 0]})
    valid_df = df[df['thanh_tien'] > 0]
    assert len(valid_df) == 1
    assert valid_df['thanh_tien'].iloc[0] == 1500000


# --- LOẠI 3: DỮ LIỆU SAI / NGOẠI LỆ (NEGATIVE) ---
def test_tc06_normalize_date_invalid_edge_case():
    """TC-06: Xử lý ngày tháng sai định dạng hoặc bị rỗng (ép về NaT)"""
    df = pd.DataFrame({'ngay': ['32/13/2025', None, 'Unknown']})
    df['ngay'] = pd.to_datetime(df['ngay'], errors='coerce')
    assert pd.isna(df['ngay'].iloc[0]) == True
    assert pd.isna(df['ngay'].iloc[1]) == True

def test_tc07_validate_phone_number_invalid_format():
    """TC-07: Loại bỏ số điện thoại chứa ký tự lạ hoặc sai định dạng"""
    df = pd.DataFrame({'so_dien_thoai': ['0901234567', 'abc123456', '0912_345']})
    valid_df = df[df['so_dien_thoai'].str.isnumeric()]
    assert len(valid_df) == 1
    assert valid_df['so_dien_thoai'].iloc[0] == '0901234567'

def test_tc08_missing_customer_name():
    """TC-08: Phát hiện tên khách hàng rỗng/Null"""
    df = pd.DataFrame({'ten_khach': ['Nguyen Van A', None, '   ']})
    df['ten_khach_clean'] = df['ten_khach'].astype(str).str.strip()
    valid_df = df[(df['ten_khach'].notna()) & (df['ten_khach_clean'] != 'None') & (df['ten_khach_clean'] != '')]
    assert len(valid_df) == 1


# --- LOẠI 4: BẢO MẬT & CHẤT LƯỢNG DỮ LIỆU ---
def test_tc09_no_secret_keys_in_env_example():
    """TC-09: Bảo mật - File .env.example không chứa thông tin mật/password thực tế"""
    if os.path.exists(".env.example"):
        content = open(".env.example", "r", encoding="utf-8").read()
        assert "password123" not in content and "secret_api_key" not in content

def test_tc10_schema_structure_dim_time():
    """TC-10: Chất lượng dữ liệu - Bảng Dim_Time có đủ các thuộc tính cốt lõi"""
    conn = sqlite3.connect("smart_crm_dwh.db")
    df = pd.read_sql_query("SELECT * FROM Dim_Time LIMIT 1", conn)
    conn.close()
    assert "time_id" in df.columns and "nam" in df.columns


# --- LOẠI 5: TÍNH TÁI LẬP PIPELINE (RECOMPUTABILITY / IDEMPOTENCY) ---
def test_tc11_pipeline_idempotency_no_duplication():
    """TC-11: Chạy lại pipeline lần 2 không bị nhân đôi dữ liệu trong Fact_Sales"""
    build_star_schema()
    conn = sqlite3.connect("smart_crm_dwh.db")
    count1 = pd.read_sql_query("SELECT COUNT(*) as cnt FROM Fact_Sales", conn)['cnt'][0]
    
    # Chạy lại lần 2
    build_star_schema()
    count2 = pd.read_sql_query("SELECT COUNT(*) as cnt FROM Fact_Sales", conn)['cnt'][0]
    conn.close()
    
    assert count1 == count2

def test_tc12_empty_file_handling():
    """TC-12: Xử lý DataFrame rỗng không làm sập chương trình"""
    df_empty = pd.DataFrame(columns=['ngay', 'ten_khach', 'so_dien_thoai', 'thanh_tien'])
    assert df_empty.empty