# Nhật ký thay đổi thiết kế (Sau BT1)

Dưới đây là các điểm điều chỉnh thiết kế kiến trúc và mô hình dữ liệu dựa trên phản hồi của giảng viên sau Bài tập 1.

| Phản hồi của Giảng viên | Quyết định điều chỉnh / Lý do kỹ thuật |
| :--- | :--- |
| **1. Sơ đồ thiếu chú thích ký hiệu.** | **Điều chỉnh:** Đã bổ sung bảng Chú thích (Legend) vào góc của cả 3 sơ đồ (Use Case, Kiến trúc, Mô hình dữ liệu). |
| **2. Tên bảng không thống nhất giữa văn bản và sơ đồ.** | **Điều chỉnh:** Đã chuẩn hóa và đồng nhất tên 4 bảng trên toàn bộ sơ đồ, văn bản và wireframe thành: `fact_sales`, `dim_date`, `dim_store`, `dim_product`. |
| **3. Các bảng Dim thiếu kiểu dữ liệu và mô tả.** | **Điều chỉnh:** Bổ sung Bảng Từ điển dữ liệu (Data Dictionary) chi tiết quy định rõ kiểu dữ liệu (Int, Varchar, Date) cho toàn bộ cột để làm cơ sở code Script ETL cho BT2. |
| **4. Đặc tả UC02 thiếu actor, điều kiện, luồng.** | **Điều chỉnh:** Cấu trúc lại đặc tả UC02 chuẩn form: thêm Actor chính, Tiền/Hậu điều kiện, Luồng sự kiện chính (đánh số 1-5) và Luồng ngoại lệ (3a, 3b). |
| **5. SRS thiếu vai trò, MoSCoW, phát biểu WON'T.** | **Điều chỉnh:** Đã bổ sung phân quyền 3 vai trò. Chuyển US08 thành phát biểu WON'T (Không làm Real-time analytics). Bổ sung cột MoSCoW vào bảng truy vết. |
| **6. Kiến trúc lặp chữ Staging, thiếu phần Ngoài phạm vi.** | **Điều chỉnh:** Xóa chữ lặp, khoanh vùng nét đứt đỏ rõ ràng cho Hệ thống POS chi nhánh (Ngoài phạm vi đồ án). |