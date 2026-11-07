# BÁO CÁO KẾT QUẢ KIỂM THỬ (TEST REPORT)

| Mã TC | Phân loại | Tiền điều kiện | Các bước thực hiện | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Minh chứng ảnh |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC-01 | Luồng đúng | Đã có file staging | Chạy `pytest tests/test_transform.py::test_tc01_normalize_date_valid` | Trả về True | Dữ liệu 1 dòng hợp lệ | PASS | `docs/screenshots/TC_ALL_PASS.png` |
| TC-02 | Luồng đúng | DB đã khởi tạo | Chạy `test_tc02_validate_thanh_tien_positive` | Xác thực số tiền > 0 | Đã lọc đúng số tiền hợp lệ | PASS | `docs/screenshots/TC_ALL_PASS.png` |
| TC-03 | Luồng đúng | Chạy luồng ETL | Chạy `test_tc03_staging_database_exists` | File DB tồn tại | Đã xác nhận file DB tồn tại | PASS | `docs/screenshots/TC_ALL_PASS.png` |
| TC-04 | Giá trị biên | Số điện thoại mẫu | Chạy `test_tc04_phone_boundary_exact_10_digits` | Độ dài = 10 chữ số | Đủ 10 chữ số | PASS | `docs/screenshots/TC_ALL_PASS.png` |
| TC-05 | Giá trị biên | Số tiền giao dịch | Chạy `test_tc05_validate_thanh_tien_negative_edge_case` | Chỉ giữ tiền > 0 | Lọc chính xác dòng > 0 | PASS | `docs/screenshots/TC_ALL_PASS.png` |
| TC-06 | Dữ liệu sai | Ngày sai định dạng | Chạy `test_tc06_normalize_date_invalid_edge_case` | Trả về NaT/Null | Trả về NaT, không sập app | PASS | `docs/screenshots/TC_ALL_PASS.png` |
| TC-07 | Dữ liệu sai | Số ĐT chứa chữ cái | Chạy `test_tc07_validate_phone_number_invalid_format` | Loại bỏ chuỗi chứa chữ | Loại bỏ thành công số lỗi | PASS | `docs/screenshots/TC_ALL_PASS.png` |
| TC-08 | Dữ liệu sai | Tên khách rỗng | Chạy `test_tc08_missing_customer_name` | Phát hiện và loại bỏ tên rỗng | Nhận diện và loại bỏ tên rỗng | PASS | `docs/screenshots/TC_ALL_PASS.png` |
| TC-09 | Bảo mật | File cấu hình | Chạy `test_tc09_no_secret_keys_in_env_example` | Không chứa Secret Key | Không có Secret Key thực tế | PASS | `docs/screenshots/TC_ALL_PASS.png` |
| TC-10 | Chất lượng DL | Database SQLite | Chạy `test_tc10_schema_structure_dim_time` | Có cột `time_id` | Tìm thấy cột `time_id` | PASS | `docs/screenshots/TC_ALL_PASS.png` |
| TC-11 | Tính tái lập | Chạy ETL 2 lần | Chạy `test_tc11_pipeline_idempotency_no_duplication` | Số dòng Fact bằng nhau | Count1 = Count2 (295 dòng) | PASS | `docs/screenshots/TC_ALL_PASS.png` |
| TC-12 | Tính tái lập | Dataframe rỗng | Chạy `test_tc12_empty_file_handling` | Bỏ qua êm đẹp | Hệ thống xử lý êm đẹp | PASS | `docs/screenshots/TC_ALL_PASS.png` |