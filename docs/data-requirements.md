# Đặc tả Yêu cầu Dữ liệu (Data Requirements Spec) - Luồng L6

## 1. Phát biểu bài toán phân tích (Analytical Questions)
* Câu hỏi 1: Tổng doanh thu và số lượng đơn hàng của từng cửa hàng theo thời gian là bao nhiêu?
* Câu hỏi 2: Dòng sản phẩm nào bán chạy nhất tại từng khu vực kinh doanh?
* Câu hỏi 3: Cửa hàng nào có tỷ lệ tăng trưởng doanh thu âm trong 3 tháng liên tiếp?

## 2. Phát biểu GRAIN (Độ hạt dữ liệu)
Mỗi dòng trong bảng sự kiện (fact_sales) thể hiện doanh thu của **MỘT sản phẩm** cụ thể được bán trong **MỘT đơn hàng** tại **MỘT cửa hàng** vào **MỘT thời điểm** nhất định.

## 3. Từ điển dữ liệu nguồn & Tỷ lệ thiếu hụt
| Tên cột nguồn | Kiểu dữ liệu | Mô tả ý nghĩa | Tỷ lệ lỗi/rỗng ước tính |
| :--- | :--- | :--- | :--- |
| Ngay | Text | Ngày mua hàng (nhiều định dạng ngày) | 0% rỗng, ~15% sai định dạng |
| Ma don | Text | Mã hóa đơn | ~2% trùng lặp mã |
| So luong | Numeric/Text| Số lượng sản phẩm bán ra | ~1% nhập nhầm bằng chữ |
| Thanh tien | Numeric | Tổng tiền (Số lượng * Đơn giá) | ~3% sai lệch tính toán |

## 4. Quy tắc chất lượng dữ liệu (Data Quality Rules)
* **DQ01 (Định dạng):** Cột Ngày bắt buộc ép về chuẩn ISO `YYYY-MM-DD`. Dòng lỗi bị đẩy vào bảng `dq_error_log`.
* **DQ02 (Tính toàn vẹn):** Không chấp nhận Số lượng hoặc Đơn giá âm (<0). 
* **DQ03 (Định danh):** `Ma don` nạp vào kho được nối thêm tiền tố Cửa hàng để đảm bảo tính Unique (VD: HCM01_DH123).