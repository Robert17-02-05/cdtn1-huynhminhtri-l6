import sqlite3

def load_data_to_db(df, db_path="smart_crm_dwh.db", table_name="staging_sales"):
    """Nạp dữ liệu sạch vào cơ sở dữ liệu SQLite"""
    conn = sqlite3.connect(db_path)
    # Dùng if_exists='replace' để đảm bảo tính re-runnable (không bị nhân đôi dữ liệu)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    
    print(f"[LOAD] Đã nạp thành công {len(df)} dòng dữ liệu vào bảng {table_name}.")