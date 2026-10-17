import pandas as pd

def clean_and_transform(df):
    """Làm sạch và chuẩn hóa định dạng ngày tháng"""
    # Chuẩn hóa cột ngày về YYYY-MM-DD (DQ01)
    df['ngay'] = pd.to_datetime(df['ngay'], format='mixed', errors='coerce').dt.strftime('%Y-%m-%d')
    
    print(f"[TRANSFORM] Đã chuẩn hóa ngày tháng cho {len(df)} dòng.")
    return df