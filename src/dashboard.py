import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

st.set_page_config(page_title="Mekong Mobile Dashboard", layout="wide")
st.title("📊 Dashboard Phân Tích Mekong Mobile (Track DA)")

# 1. Kết nối và lấy dữ liệu từ DWH
@st.cache_data
def load_data():
    conn = sqlite3.connect('smart_crm_dwh.db')
    # Lấy doanh thu và số đơn hàng theo tháng
    query = """
        SELECT t.thang, t.nam, SUM(f.thanh_tien) as tong_doanh_thu, COUNT(f.so_dien_thoai) as so_don_hang
        FROM Fact_Sales f
        JOIN Dim_Time t ON f.time_id = t.time_id
        GROUP BY t.nam, t.thang
        ORDER BY t.nam, t.thang
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    if not df.empty:
        df['thang_nam'] = df['thang'].astype(str) + '/' + df['nam'].astype(str)
    return df

df = load_data()

if df.empty:
    st.warning("Không có dữ liệu để hiển thị. Vui lòng kiểm tra lại DWH.")
else:
    col1, col2 = st.columns(2)

    # --- BIỂU ĐỒ 1: DOANH THU CÓ MỐC TRUNG BÌNH ---
    with col1:
        st.subheader("1. Doanh thu theo tháng")
        fig1, ax1 = plt.subplots(figsize=(8, 4))
        ax1.bar(df['thang_nam'], df['tong_doanh_thu'], color='#3498db', label='Doanh thu thực tế')
        
        # Mốc tham chiếu: Đường trung bình doanh thu
        mean_rev = df['tong_doanh_thu'].mean()
        ax1.axhline(mean_rev, color='red', linestyle='--', linewidth=2, label=f'Trung bình: {mean_rev:,.0f} VNĐ')
        
        ax1.set_ylabel("VNĐ")
        ax1.tick_params(axis='x', rotation=45)
        ax1.legend()
        st.pyplot(fig1)

    # --- BIỂU ĐỒ 2: SỐ LƯỢNG ĐƠN HÀNG CÓ MỐC SLA ---
    with col2:
        st.subheader("2. Số lượng đơn hàng & SLA")
        fig2, ax2 = plt.subplots(figsize=(8, 4))
        ax2.plot(df['thang_nam'], df['so_don_hang'], marker='o', color='#2ecc71', linewidth=2, label='Đơn hàng thực tế')
        
        # Mốc so sánh SLA: Mục tiêu 15 đơn/tháng (giả định)
        sla_target = 15
        ax2.axhline(sla_target, color='#e67e22', linestyle='-', linewidth=2, label=f'Mục tiêu SLA ({sla_target} đơn)')
        
        ax2.set_ylabel("Số lượng")
        ax2.tick_params(axis='x', rotation=45)
        ax2.legend()
        st.pyplot(fig2)