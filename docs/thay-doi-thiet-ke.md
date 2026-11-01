# Nhật ký thay đổi thiết kế so với Bài tập 1

Tài liệu này ghi nhận các thay đổi về thiết kế và kiến trúc nhằm khắc phục lỗi từ Bài tập 1 và phản ánh đúng thực tế khi hiện thực mã nguồn ở Bài tập 2.

## 1. Khắc phục lỗi thiết kế Bài tập 1 (Theo feedback giảng viên)

| Phản hồi của Giảng viên | Quyết định điều chỉnh / Lý do kỹ thuật |
| :--- | :--- |
| **Sơ đồ thiếu chú thích ký hiệu.** | **Điều chỉnh:** Đã bổ sung bảng Chú thích (Legend) vào góc của cả 3 sơ đồ (Use Case, Kiến trúc, Mô hình dữ liệu). |
| **Tên bảng không thống nhất giữa văn bản và sơ đồ.** | **Điều chỉnh:** Đã chuẩn hóa và đồng nhất tên 4 bảng trên toàn bộ sơ đồ, văn bản và wireframe thành: `fact_sales`, `dim_date`, `dim_store`, `dim_product`. |
| **Các bảng Dim thiếu kiểu dữ liệu và mô tả.** | **Điều chỉnh:** Bổ sung Bảng Từ điển dữ liệu (Data Dictionary) chi tiết quy định rõ kiểu dữ liệu (Int, Varchar, Date) cho toàn bộ cột để làm cơ sở code Script ETL cho BT2. |
| **Đặc tả UC02 thiếu actor, điều kiện, luồng.** | **Điều chỉnh:** Cấu trúc lại đặc tả UC02 chuẩn form: thêm Actor chính, Tiền/Hậu điều kiện, Luồng sự kiện chính (đánh số 1-5) và Luồng ngoại lệ (3a, 3b). |
| **SRS thiếu vai trò, MoSCoW, phát biểu WON'T.** | **Điều chỉnh:** Đã bổ sung phân quyền 3 vai trò. Chuyển US08 thành phát biểu WON'T (Không làm Real-time analytics). Bổ sung cột MoSCoW vào bảng truy vết. |
| **Kiến trúc lặp chữ Staging, thiếu Ngoài phạm vi.** | **Điều chỉnh:** Xóa chữ lặp, khoanh vùng nét đứt đỏ rõ ràng cho Hệ thống POS chi nhánh (Ngoài phạm vi đồ án). |

## 2. Thay đổi thiết kế phát sinh trong quá trình hiện thực (Bài tập 2)

* **Thay đổi:** Gộp và đổi tên bảng chiều `dim_product`, `dim_store` thành `Dim_Customer`. Tên bảng viết hoa chữ cái đầu (`Fact_Sales`, `Dim_Time`) thay vì viết thường như BT1. Tóm lại, Script ETL thực tế tạo ra 3 bảng: `Dim_Time`, `Dim_Customer`, `Fact_Sales`.
* **Vì sao:** Trong quá trình trích xuất và biến đổi dữ liệu thực tế (Sprint 1), dữ liệu từ staging tập trung mạnh vào thông tin khách hàng (`ten_khach`, `so_dien_thoai`) nên việc xây dựng `Dim_Customer` khả thi và phản ánh đúng thực tế nghiệp vụ hơn việc tách bảng sản phẩm/cửa hàng.
* **Ảnh hưởng:** 
   - Mã nguồn `src/load/dwh_builder.py` được tinh chỉnh để nạp dữ liệu vào cấu trúc 3 bảng mới.
   - Truy vấn SQL trong giao diện `src/dashboard.py` kết nối trực tiếp vào `Fact_Sales` và `Dim_Time` để thống kê.