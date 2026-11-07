# NHẬT KÝ SỬA LỖI (BUG LOG)

### BUG-01 (Critical) - Crash luồng ETL khi gặp định dạng ngày không hợp lệ
1. **Mã bug & Mức độ:** BUG-01 · Critical
2. **Phát hiện bởi:** Sinh viên tự chạy test (TC-06)
3. **Triệu chứng:** Tiến trình ETL dừng đột ngột với lỗi `ValueError: Unknown string format` khi đọc dòng ngày lỗi.
4. **Cách tái lập:** Đưa chuỗi `32/13/2025` vào cột `ngay` và chạy `python src/load/dwh_builder.py`.
5. **Nguyên nhân:** Hàm `pd.to_datetime` chưa bật tham số xử lý lỗi ngoại lệ `errors='coerce'`.
6. **Cách sửa:** Thêm `errors='coerce'` và loại bỏ các dòng `NaT` trước khi sinh `time_id`.
7. **Commit xác nhận:** [Link Commit BUG-01]([https://github.com/Robert17-02-05/cdtn1-huynhminhtri-l6/commit/7becf00994fbf09e620b11e497b5c11bab78c911](https://github.com/Robert17-02-05/cdtn1-huynhminhtri-l6/commit/7becf00994fbf09e620b11e497b5c11bab78c911))

---

### BUG-02 (Major) - Trùng lặp khóa chính time_id trong bảng Dim_Time
1. **Mã bug & Mức độ:** BUG-02 · Major
2. **Phát hiện bởi:** Kiểm tra chất lượng dữ liệu (TC-11)
3. **Triệu chứng:** Bảng Dim_Time chứa các dòng trùng lặp mã `time_id` khi cùng ngày giao dịch.
4. **Cách tái lập:** Chạy nạp dữ liệu với staging có nhiều giao dịch trong cùng 1 ngày.
5. **Nguyên nhân:** Thiếu bước lọc loại bỏ dữ liệu trùng lặp trên Dataframe trước khi nạp vào DB.
6. **Cách sửa:** Thêm phương thức `.drop_duplicates(subset=['time_id'])` khi tạo `dim_time`.
7. **Commit xác nhận:** [Link Commit BUG-02]([https://github.com/Robert17-02-05/cdtn1-huynhminhtri-l6/commit/696767460e65ecf64ee27dad17e99d97217bae9c](https://github.com/Robert17-02-05/cdtn1-huynhminhtri-l6/commit/696767460e65ecf64ee27dad17e99d97217bae9c))

---

### BUG-03 (Minor) - Dư thừa khoảng trắng ở tên khách hàng gây phân mảnh dữ liệu
1. **Mã bug & Mức độ:** BUG-03 · Minor
2. **Phát hiện bởi:** Chạy test dữ liệu sai (TC-08)
3. **Triệu chứng:** Khách hàng "Nguyen Van A " và "Nguyen Van A" bị tính thành 2 khách hàng khác nhau.
4. **Cách tái lập:** Kiểm tra dữ liệu nạp vào bảng Dim_Customer.
5. **Nguyên nhân:** Chưa chuẩn hóa cắt khoảng trắng ở hai đầu chuỗi văn bản.
6. **Cách sửa:** Áp dụng `.str.strip()` cho thuộc tính `ten_khach`.
7. **Commit xác nhận:** [Link Commit BUG-03]([https://github.com/Robert17-02-05/cdtn1-huynhminhtri-l6/commit/b63b14a84fbb36d95f3f8d64948c2146cb40212d](https://github.com/Robert17-02-05/cdtn1-huynhminhtri-l6/commit/b63b14a84fbb36d95f3f8d64948c2146cb40212d))