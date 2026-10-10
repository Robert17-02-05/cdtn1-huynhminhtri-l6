# Đặc tả yêu cầu phần mềm (SRS) - Luồng L6: Kho dữ liệu bán hàng (Smart CRM DWH)

## 1. Tổng quan hệ thống
**1.1. Phạm vi dự án**
Dự án tập trung xây dựng Kho dữ liệu báo cáo (Smart CRM DWH) cho chuỗi Mekong Mobile. Hệ thống sẽ tự động hóa luồng trích xuất (ETL) dữ liệu đơn hàng từ 24 file Excel của các chi nhánh, làm sạch các lỗi định dạng và nạp vào kho dữ liệu tập trung. Mục tiêu giải quyết vấn đề trễ nải số liệu và cung cấp Dashboard trực quan đa chiều cho Ban giám đốc.

**1.2. Người dùng chính (Actor)**
*   **Chuyên viên dữ liệu (Data Engineer):** Vận hành tiến trình ETL, theo dõi log lỗi.
*   **Quản lý cửa hàng:** Xem báo cáo doanh thu cấp độ chi nhánh.
*   **Ban giám đốc:** Phân tích doanh thu toàn hệ thống, xem xu hướng và đưa ra quyết định kinh doanh.

**1.3. Bảng thuật ngữ (Glossary)**
| Thuật ngữ / Viết tắt | Ý nghĩa / Định nghĩa chi tiết |
| :--- | :--- |
| **DWH (Data Warehouse)** | Kho dữ liệu tập trung, được thiết kế theo Lược đồ hình sao (Star Schema). |
| **ETL** | Trích xuất (Extract) - Biến đổi/Làm sạch (Transform) - Nạp dữ liệu (Load). |
| **Staging Area** | Vùng đệm lưu trữ dữ liệu tạm thời trước khi nạp chính thức vào DWH. |
| **GWT** | Given – When – Then, dùng để mô tả tiêu chí chấp nhận (Acceptance Criteria). |
| **MoSCoW** | Phương pháp đánh giá độ ưu tiên: MUST, SHOULD, COULD, WON'T. |

## 2. Danh sách User Story

| Mã | Vai trò | Nội dung (Tôi muốn... để...) | Ưu tiên |
| :--- | :--- | :--- | :--- |
| **US01** | Phó Tổng giám đốc | Xem báo cáo doanh thu mỗi tháng của từng cửa hàng để biết nơi nào kinh doanh đi xuống. | MUST |
| **US02** | Quản lý cửa hàng | Xem báo cáo doanh thu theo ngày của chi nhánh mình và so sánh với cửa hàng khác. | MUST |
| **US03** | Ban giám đốc | Hệ thống tự động tổng hợp dữ liệu từ 24 cửa hàng để không phải chờ tổng hợp thủ công. | MUST |
| **US04** | Chuyên viên DL | Script ETL tự động chuẩn hóa định dạng (ngày tháng, tiền tệ) để nạp dữ liệu sạch vào kho. | MUST |
| **US05** | Ban giám đốc | Phân tích doanh thu theo chiều sản phẩm và cửa hàng để biết dòng máy bán chạy nhất. | MUST |
| **US06** | Chuyên viên DL | Hệ thống tự động ghi log dữ liệu lỗi vào bảng `dq_error_log` để tiện đối soát với chi nhánh. | SHOULD |
| **US07** | Ban giám đốc | Xem biểu đồ xu hướng (Trendline) để so sánh doanh thu cùng kỳ năm ngoái. | COULD |
| **US08** | Chuyên viên DL | Hệ thống từ chối nạp bản ghi có số lượng/đơn giá âm để bảo vệ tính toàn vẹn tài chính. | MUST |

## 3. Use Case & Đặc tả chi tiết

**3.1. Danh sách Use Case**
| Mã UC | Tên Use Case | Actor thực hiện | Phân loại |
| :--- | :--- | :--- | :--- |
| **UC01** | Trích xuất dữ liệu Excel | Chuyên viên dữ liệu | MUST |
| **UC02** | Làm sạch và chuẩn hóa dữ liệu | Chuyên viên dữ liệu | MUST |
| **UC03** | Ghi log lỗi vào Database | Hệ thống (`<<include>>`) | MUST |
| **UC04** | Cảnh báo lỗi cấu trúc | Hệ thống (`<<extend>>`) | SHOULD |
| **UC05** | Nạp dữ liệu vào DWH | Chuyên viên dữ liệu | MUST |
| **UC06** | Xem báo cáo chi nhánh | Quản lý cửa hàng | MUST |
| **UC07** | Xem báo cáo tổng hợp | Ban giám đốc | MUST |
| **UC08** | Phân tích đa chiều | Ban giám đốc | MUST |

**3.2. Đặc tả Use Case UC02: Làm sạch và chuẩn hóa dữ liệu**
*   **Mô tả:** Tiến trình ETL đọc dữ liệu thô, loại bỏ rác, ép kiểu ngày tháng và tính toán lại trường doanh thu.
*   **Tiêu chí chấp nhận (GWT):**
    *   **GWT01 (Chuẩn hóa ngày):** *Given* ngày mua có định dạng tự do, *When* chạy Transform, *Then* hệ thống lưu trữ dưới chuẩn duy nhất `YYYY-MM-DD`.
    *   **GWT02 (Tính thành tiền):** *Given* cột Thành tiền bị sai, *When* chạy luồng xử lý, *Then* hệ thống tự động tính lại bằng công thức `So luong * Don gia`.
    *   **GWT03 (Xử lý lỗi - Ngoại lệ):** *Given* dữ liệu chứa số lượng âm hoặc khoảng trống, *When* ép kiểu thất bại, *Then* hệ thống ghi dòng đó vào `dq_error_log` (UC03) và tiếp tục xử lý dòng tiếp theo.

## 4. Yêu cầu chức năng (FR) và Phi chức năng (NFR)

**4.1. Yêu cầu chức năng**
| Mã | Mô tả yêu cầu hệ thống |
| :--- | :--- |
| **FR01** | Hệ thống phải đọc và trích xuất thành công dữ liệu từ định dạng `.xlsx` trong thư mục nguồn. |
| **FR02** | Hệ thống phải tự động tính toán lại cột "Thành tiền" = Số lượng x Đơn giá. |
| **FR03** | Hệ thống phải chuẩn hóa mọi định dạng thời gian về chuẩn ISO 8601 (`YYYY-MM-DD`). |
| **FR04** | Hệ thống phải phát hiện bản ghi lỗi (âm, thiếu mã) và ghi vào bảng `dq_error_log`. |

**4.2. Yêu cầu phi chức năng**
| Mã | Tiêu chí | Ngưỡng đo lường bắt buộc |
| :--- | :--- | :--- |
| **NFR01** | Hiệu năng | Thời gian chạy luồng ETL cho 50,000 dòng từ 24 file **≤ 3 phút**. |
| **NFR02** | Tính khả dụng| Dashboard báo cáo trên Web phản hồi thao tác lọc **≤ 3 giây**. |
| **NFR03** | Độ tin cậy | Luồng ETL không crash khi gặp file hỏng, ghi log lỗi thành công **100%**. |

## 5. Bảng truy vết yêu cầu (Traceability Matrix)
| ID Nguồn (User Story) | Use Case tương ứng | Yêu cầu hệ thống (FR/NFR) | Trạng thái |
| :--- | :--- | :--- | :--- |
| **US03** | UC01, UC05 | FR01, NFR01 | Đã thiết kế |
| **US04, US08** | UC02, UC04 | FR02, FR03, FR04 | Đã thiết kế |
| **US06** | UC03 | FR04, NFR03 | Đã thiết kế |
| **US01, US05, US07** | UC07, UC08 | NFR02 | Đã thiết kế |
| **US02** | UC06 | NFR02 | Đã thiết kế |