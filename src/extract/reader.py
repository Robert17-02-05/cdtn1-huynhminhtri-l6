import pandas as pd
import os

def read_sales_data(file_path):
    """Đọc dữ liệu nguồn từ file CSV"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Không tìm thấy file: {file_path}")
    
    df = pd.read_csv(file_path)
    print(f"[EXTRACT] Đã đọc thành công {len(df)} dòng dữ liệu từ {file_path}")
    return df