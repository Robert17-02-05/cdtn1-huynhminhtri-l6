# Đặc tả yêu cầu phần mềm (SRS) - Luồng L6: Kho dữ liệu bán hàng

## 1. Bảng thuật ngữ (Glossary)
| Thuật ngữ / Viết tắt | Ý nghĩa / Định nghĩa chi tiết |
| :--- | :--- |
| **DWH (Data Warehouse)** | Kho dữ liệu tập trung chứa dữ liệu đã được làm sạch để phục vụ phân tích. |
| **ETL** | Extract, Transform, Load - Quy trình trích xuất, biến đổi (làm sạch) và nạp dữ liệu. |
| **Staging** | Vùng lưu trữ dữ liệu tạm thời trước khi nạp chính thức vào DWH. |

## 2. Tổng quan hệ thống (Overview)
Hệ thống Kho dữ liệu báo cáo (Smart CRM DWH) tự động hóa việc thu thập, làm sạch dữ liệu đơn hàng từ 24 file Excel của các chi nhánh. Hệ thống giúp loại bỏ sai sót thủ công và cung cấp Dashboard trực quan đa chiều cho Ban giám đốc ra quyết định.

## 3. Danh sách User Story
* **US1:** Là Phó Tổng giám đốc, tôi muốn xem báo cáo tổng hợp doanh thu mỗi tháng của từng cửa hàng để biết được cửa hàng nào đang kinh doanh đi xuống (MUST).
* **US2:** Là Quản lý cửa hàng, tôi muốn xem báo cáo doanh thu theo ngày của chi nhánh mình và so sánh với các cửa hàng khác (MUST).
* **US3:** Là Ban giám đốc, tôi muốn hệ thống tự động tổng hợp dữ liệu doanh thu từ 24 cửa hàng để không phải chờ đợi 5-7 ngày thủ công (MUST).
* **US4:** Là Chuyên viên dữ liệu, tôi muốn script ETL tự động chuẩn hóa các cột lỗi (ngày tháng, tiền tệ) để nạp dữ liệu sạch vào kho (MUST).
* **US5:** Là Ban giám đốc, tôi muốn phân tích doanh thu theo chiều sản phẩm và cửa hàng để biết dòng máy bán chạy nhất (MUST).
* **US6:** Là Chuyên viên DL, tôi muốn hệ thống tự động ghi log dòng dữ liệu lỗi vào bảng `dq_error_log` (SHOULD).
* **US7:** Là Ban giám đốc, tôi muốn xem biểu đồ xu hướng (Trendline) so sánh doanh thu cùng kỳ năm ngoái (COULD).
* **US8:** Là Chuyên viên DL, tôi muốn CSDL từ chối nạp bản ghi có số lượng/đơn giá âm (MUST).

## 4. Danh sách Use Case & Đặc tả
* **Danh sách Actor:** Chuyên viên dữ liệu, Quản lý cửa hàng, Ban giám đốc.
* **Danh sách Use Case:** (1) Trích xuất dữ liệu, (2) Làm sạch dữ liệu, (3) Ghi log lỗi `<<include>>`, (4) Báo lỗi cấu trúc `<<extend>>`, (5) Nạp dữ liệu vào DWH, (6) Xem báo cáo chi nhánh, (7) Xem báo cáo tổng hợp, (8) Phân tích đa chiều.
* **Đặc tả Use Case UC02: Làm sạch và chuẩn hóa dữ liệu**
  * **Tiền điều kiện:** Trích xuất file Excel thành công.
  * **Luồng chính:** (1) Actor chạy lệnh Transform. (2) Hệ thống chuẩn hóa định dạng thời gian YYYY-MM-DD và số tiền. (3) Tạo định danh "Mã_Đơn_Mới". (4) Đẩy dòng hợp lệ vào Staging.
  * **Luồng ngoại lệ:** Nếu dữ liệu hỏng nặng không thể ép kiểu, hệ thống kích hoạt UC03 (Ghi log), lưu vào bảng `dq_error_log` và tự động xử lý dòng tiếp theo (không crash).

## 5. Yêu cầu chức năng (FR) và Phi chức năng (NFR)
* **FR01:** Hệ thống phải có khả năng trích xuất dữ liệu từ các file `.xlsx` trong thư mục chỉ định.
* **FR02:** Hệ thống phải tự động tính toán lại cột "Thành tiền" dựa trên "Số lượng" và "Đơn giá".
* **NFR01 (Hiệu năng):** Thời gian chạy toàn bộ tiến trình ETL cho 24 file (khoảng 50,000 dòng) không được vượt quá 3 phút.
* **NFR02 (Tính khả dụng):** Dashboard phải tải và phản hồi các thao tác lọc dữ liệu dưới 3 giây.

## 6. Bảng truy vết yêu cầu (Traceability Matrix)
| ID Nguồn (User Story) | Use Case tương ứng | Yêu cầu hệ thống (FR/NFR) | Trạng thái |
| :--- | :--- | :--- | :--- |
| US3 | UC01, UC05 | FR01, NFR01 | Đã thiết kế |
| US4, US8 | UC02, UC03 | FR02 | Đã thiết kế |
| US1, US5 | UC07, UC08 | NFR02 | Đã thiết kế |