import pandas as pd
import sqlite3

def validate_and_reject(df, db_path="smart_crm_dwh.db"):
    """Lọc các dòng có thành tiền âm, đẩy vào bảng dq_error_log"""
    
    # Ép kiểu cột thanh_tien về dạng số (nếu có chữ hoặc ký tự rác thì chuyển thành NaN)
    df['thanh_tien'] = pd.to_numeric(df['thanh_tien'], errors='coerce')
    
    # Điều kiện lỗi: thanh_tien < 0 hoặc bị NaN (rỗng/lỗi định dạng)
    error_mask = (df['thanh_tien'] < 0) | (df['thanh_tien'].isna())
    
    df_error = df[error_mask].copy()
    df_valid = df[~error_mask].copy()
    
    # Ghi dòng lỗi vào bảng reject (dq_error_log) trong SQLite
    if not df_error.empty:
        df_error['error_reason'] = "Giá trị thành tiền bị âm hoặc không hợp lệ (DQ02)"
        
        conn = sqlite3.connect(db_path)
        df_error.to_sql('dq_error_log', conn, if_exists='append', index=False)
        conn.close()
        print(f"[QUALITY] Phát hiện và đã ghi log {len(df_error)} dòng dữ liệu lỗi vào dq_error_log.")
        
    return df_valid