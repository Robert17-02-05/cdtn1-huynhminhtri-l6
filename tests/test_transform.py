import pandas as pd
import pytest

# TEST 1: Luồng chuẩn - Xử lý định dạng ngày tháng hợp lệ
def test_normalize_date_valid():
    df = pd.DataFrame({'ngay': ['2024-05-15', '15/06/2025']})
    df['ngay'] = pd.to_datetime(df['ngay'], errors='coerce')
    assert df['ngay'].dt.year.iloc[0] == 2024

# TEST 2: Luồng ngoại lệ - Xử lý ngày tháng sai định dạng hoặc bị rỗng (Edge case)
def test_normalize_date_invalid_edge_case():
    df = pd.DataFrame({'ngay': ['32/13/2025', None, 'Unknown']})
    df['ngay'] = pd.to_datetime(df['ngay'], errors='coerce')
    # Tất cả các giá trị sai phải bị ép về NaT (Not a Time)
    assert pd.isna(df['ngay'].iloc[0]) == True
    assert pd.isna(df['ngay'].iloc[1]) == True

# TEST 3: Luồng chuẩn - Xác thực số tiền thanh toán hợp lệ (>0)
def test_validate_thanh_tien_positive():
    df = pd.DataFrame({'thanh_tien': [1500000, 500000]})
    valid_df = df[df['thanh_tien'] > 0]
    assert len(valid_df) == 2

# TEST 4: Giá trị biên - Xử lý giao dịch có số tiền âm hoặc bằng 0 (Edge case)
def test_validate_thanh_tien_negative_edge_case():
    df = pd.DataFrame({'thanh_tien': [1500000, -50000, 0]})
    # Chỉ giữ lại dòng có tiền > 0
    valid_df = df[df['thanh_tien'] > 0]
    assert len(valid_df) == 1
    assert valid_df['thanh_tien'].iloc[0] == 1500000

# TEST 5: Luồng chuẩn - Xác thực dữ liệu chuỗi (số điện thoại không chứa ký tự lạ)
def test_validate_phone_number_format():
    df = pd.DataFrame({'so_dien_thoai': ['0901234567', 'abc123456', '0912_345']})
    # Lọc ra các số điện thoại chỉ chứa chữ số
    valid_df = df[df['so_dien_thoai'].str.isnumeric()]
    assert len(valid_df) == 1
    assert valid_df['so_dien_thoai'].iloc[0] == '0901234567'