# Đặc tả Yêu cầu Dữ liệu (Data Requirements Spec) - Luồng L6

## 1. Phát biểu bài toán phân tích (Analytical Questions)
- **Câu hỏi 1:** Tổng doanh thu và số lượng đơn hàng của từng cửa hàng theo thời gian là bao nhiêu?
- **Câu hỏi 2:** Dòng sản phẩm nào bán chạy nhất tại từng khu vực kinh doanh?
- **Câu hỏi 3:** Cửa hàng nào có tỷ lệ tăng trưởng doanh thu âm trong 3 tháng liên tiếp?

## 2. Đặc tả dữ liệu nguồn (Source Data)
*   **Tên file mẫu:** `DonHang_<TenCuaHang>_<Thang>.xlsx`
*   **Tần suất nạp:** Hàng ngày (Daily Batch).
*   **Mô tả:** Dữ liệu đơn hàng thô được tổng hợp từ 24 chi nhánh cửa hàng.

| Tên cột Excel | Kiểu dữ liệu thô | Mô tả ý nghĩa | Tỷ lệ lỗi/rỗng ước tính |
| :--- | :--- | :--- | :--- |
| `Ngay` | Văn bản (Text) | Ngày mua hàng (nhiều định dạng lộn xộn) | 0% rỗng, ~15% sai định dạng |
| `Ma don` | Văn bản (Text) | Mã hóa đơn | ~2% trùng lặp mã giữa các chi nhánh |
| `San pham` | Văn bản (Text) | Tên sản phẩm bán ra | Chứa sai chính tả, ghi không thống nhất |
| `So luong` | Số / Text | Số lượng sản phẩm bán ra | ~1% nhập nhầm bằng ký tự chữ ("hai") |
| `Don gia` | Số / Text | Đơn giá sản phẩm | Có chứa đơn vị tiền tệ ("VND") |
| `Thanh tien` | Numeric | Tổng tiền (Số lượng * Đơn giá) | ~3% sai lệch do tính toán thủ công |

## 3. Quy tắc chất lượng dữ liệu (Data Quality Rules)
- **DQ01 (Định dạng thời gian):** Cột Ngày bắt buộc ép về chuẩn ISO `YYYY-MM-DD`. Dòng lỗi không ép kiểu được bị đẩy vào bảng `dq_error_log`.
- **DQ02 (Tính toàn vẹn giá trị):** Không chấp nhận Số lượng hoặc Đơn giá âm (<0). Các cột `So luong`, `Don gia` phải được tự động làm sạch các ký tự chữ cái, khoảng trắng trước khi ép sang kiểu số.
- **DQ03 (Định danh duy nhất):** `Ma don` nạp vào kho được nối thêm tiền tố Cửa hàng để đảm bảo tính Unique (VD: HCM01_DH123) và sinh Surrogate Key tự động.
- **DQ04 (Chuẩn hóa tính toán):** Bỏ qua giá trị cột `Thanh tien` từ file Excel nguồn. Hệ thống phải tự động tính toán lại bằng công thức `So luong * Don gia` để triệt tiêu tỷ lệ sai lệch 3%.

## 4. Ánh xạ dữ liệu đích (Target Mapping) & Độ hạt
**Phát biểu GRAIN (Độ hạt dữ liệu):** 
Mỗi dòng trong bảng sự kiện (`fact_sales`) thể hiện doanh thu của **MỘT sản phẩm** cụ thể được bán trong **MỘT đơn hàng** tại **MỘT cửa hàng** vào **MỘT thời điểm** nhất định.

**Bảng ánh xạ vào `fact_sales`:**
| Cột đích trong `fact_sales` | Kiểu dữ liệu | Nguồn trích xuất / Logic tính toán (ETL Rule) |
| :--- | :--- | :--- |
| `date_key` | Integer (FK) | Trích xuất từ cột `Ngay` (áp dụng DQ01) -> Lookup lấy ID từ `dim_date`. |
| `store_key` | Integer (FK) | Trích xuất từ Tên file Excel tải lên -> Lookup lấy ID từ `dim_store`. |
| `product_key` | Integer (FK) | Trích xuất từ cột `San pham` -> Lookup lấy ID từ `dim_product`. |
| `quantity` | Integer | Lấy trực tiếp từ cột `So luong` (áp dụng DQ02). |
| `total_amount` | Numeric | Tính tự động bằng công thức: `So luong * Don gia` (áp dụng DQ04). |