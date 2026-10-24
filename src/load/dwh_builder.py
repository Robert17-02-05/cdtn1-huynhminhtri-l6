import sqlite3
import pandas as pd

def build_star_schema(db_path="smart_crm_dwh.db"):
    # Kết nối vào cơ sở dữ liệu SQLite hiện tại
    conn = sqlite3.connect(db_path)
    print("--- BẮT ĐẦU CHUYỂN HÓA VÀ NẠP DỮ LIỆU STAR SCHEMA ---")
    
    # 1. Đọc dữ liệu sạch từ bảng staging_sales
    try:
        df_staging = pd.read_sql_query("SELECT * FROM staging_sales", conn)
    except Exception as e:
        print("Không tìm thấy bảng staging_sales. Hãy đảm bảo SPRINT 1 đã chạy thành công.")
        return

    # 2. Xây dựng bảng chiều thời gian (Dim_Time)
    # Chuyển đổi cột ngày sang định dạng datetime để tách thông tin
    df_staging['ngay'] = pd.to_datetime(df_staging['ngay'], errors='coerce')
    
    dim_time = pd.DataFrame({
        'time_id': df_staging['ngay'].dt.strftime('%Y%m%d'),
        'ngay_trong_thang': df_staging['ngay'].dt.day,
        'thang': df_staging['ngay'].dt.month,
        'quy': df_staging['ngay'].dt.quarter,
        'nam': df_staging['ngay'].dt.year
    }).dropna().drop_duplicates(subset=['time_id']).reset_index(drop=True)
    
    # Lưu Dim_Time vào DB
    dim_time.to_sql('Dim_Time', conn, if_exists='replace', index=False)
    print(f"[DWH] Đã nạp thành công {len(dim_time)} dòng vào bảng Dim_Time.")

    # 3. Xây dựng bảng chiều khách hàng (Dim_Customer)
    # Trích xuất từ các cột có sẵn trên staging (ten_khach, so_dien_thoai)
    if 'so_dien_thoai' in df_staging.columns and 'ten_khach' in df_staging.columns:
        dim_customer = df_staging[['so_dien_thoai', 'ten_khach']].dropna().drop_duplicates(subset=['so_dien_thoai']).reset_index(drop=True)
        dim_customer.to_sql('Dim_Customer', conn, if_exists='replace', index=False)
        print(f"[DWH] Đã nạp thành công {len(dim_customer)} khách hàng vào bảng Dim_Customer.")

    # 4. Xây dựng bảng sự kiện bán hàng (Fact_Sales)
    # Giữ lại các khóa (Keys) và số liệu đo lường (Metrics như thanh_tien)
    fact_sales = df_staging.copy()
    fact_sales['time_id'] = fact_sales['ngay'].dt.strftime('%Y%m%d')
    
    # Tùy chỉnh các cột cần thiết cho Fact Table
    fact_cols = ['time_id', 'so_dien_thoai', 'thanh_tien']
    
    # Nếu dữ liệu ban đầu của bạn có các cột san_pham, cua_hang thì tự động đưa vào
    if 'san_pham' in fact_sales.columns: fact_cols.append('san_pham')
    if 'cua_hang' in fact_sales.columns: fact_cols.append('cua_hang')
    if 'nhan_vien' in fact_sales.columns: fact_cols.append('nhan_vien')

    # Lọc cột và nạp vào DB
    fact_sales = fact_sales[fact_cols]
    fact_sales.to_sql('Fact_Sales', conn, if_exists='replace', index=False)
    print(f"[DWH] Đã nạp thành công {len(fact_sales)} giao dịch vào bảng Fact_Sales.")
    
    conn.close()
    print("--- HOÀN TẤT XÂY DỰNG KHO DỮ LIỆU DWH ---")

if __name__ == "__main__":
    build_star_schema()