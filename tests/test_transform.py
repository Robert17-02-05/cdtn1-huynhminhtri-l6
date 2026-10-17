import pandas as pd
import sys
import os

# Thêm thư mục src vào đường dẫn để import được module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from transform.cleaner import clean_and_transform

def test_clean_date():
    # 1. Given (Dữ liệu giả lập có các định dạng ngày tháng khác nhau)
    df_mock = pd.DataFrame({
        'ngay': ['2026.01.30', '15-10-25', 'sai_dinh_dang']
    })
    
    # 2. When (Chạy hàm làm sạch)
    df_result = clean_and_transform(df_mock)
    
    # 3. Then (Kiểm tra kết quả chuẩn hóa ISO YYYY-MM-DD)
    assert df_result['ngay'].iloc[0] == '2026-01-30', "Lỗi chuẩn hóa ngày tháng 1!"
    assert df_result['ngay'].iloc[1] == '2025-10-15', "Lỗi chuẩn hóa ngày tháng 2!"
    assert pd.isna(df_result['ngay'].iloc[2]), "Không bắt được lỗi định dạng ngày!"
    print("Unit Test PASS: Ngày tháng được chuẩn hóa chính xác.")