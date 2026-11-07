# KẾ HOẠCH KIỂM THỬ PIPELINE VÀ DWH (TEST PLAN) - TRACK DA (LUỒNG L6)

## 1. Phạm vi kiểm thử
- **Trong phạm vi (In-Scope):** Luồng ETL trích xuất file CSV/Excel (`src/extract/`), làm sạch dữ liệu (`src/transform/`), nạp dữ liệu vào SQLite DWH Star Schema (`src/load/dwh_builder.py`), báo cáo log lỗi (`dq_error_log`), và giao diện Streamlit (`src/dashboard.py`).
- **Ngoài phạm vi (Out-of-Scope):** Gửi email cảnh báo tự động, tích hợp dữ liệu Real-time POS.

## 2. Chiến lược và Loại kiểm thử (Đủ 5 loại)
1. **Luồng đúng (Happy Path):** Dữ liệu chuẩn nạp thành công 100%, số bản ghi khớp.
2. **Giá trị biên (Boundary):** Độ dài SĐT đúng 10 chữ số; ngày ở ranh giới tháng/năm.
3. **Dữ liệu sai (Negative):** Ngày hỏng định dạng, thiếu tên khách, doanh thu âm/rỗng.
4. **Chất lượng dữ liệu/Bảo mật:** Không lọt bản ghi rác vào Fact/Dim, không lộ biến môi trường.
5. **Tính tái lập (Reposibility):** Chạy lại pipeline lần 2 không bị nhân đôi dữ liệu (`if_exists='replace'`).

## 3. Tiêu chí thành công & Môi trường
- **Tiêu chí:** 100% test cases trong bộ kiểm thử `pytest` đạt PASS; pipeline chạy lại từ thư mục trống bằng 1 lệnh không sập.
- **Môi trường:** Python 3.14, SQLite3, Pytest 9.x, Streamlit, Windows 11.