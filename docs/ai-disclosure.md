# Khai báo sử dụng công cụ AI hỗ trợ

### II. BẢNG KHAI BÁO CHI TIẾT

| Hạng mục khai báo | Nội dung chi tiết |
| :--- | :--- |
| **1. Công cụ AI sử dụng** | Google Gemini. |
| **2. Mục đích sử dụng** | - Hỗ trợ tìm kiếm ý tưởng và cấu trúc bài báo cáo.<br>- Tinh chỉnh văn phong chuyên ngành, định dạng văn bản.<br>- Hỗ trợ tạo khung (skeleton) mã nguồn để vẽ sơ đồ, wireframe. |
| **3. Cách thức kiểm chứng** | - Rà soát và đọc hiểu thủ công toàn bộ nội dung văn bản.<br>- Đối chiếu chéo các quy tắc, biểu đồ với tài liệu hướng dẫn của học phần và Case study gốc.<br>- Tự kiểm tra tính logic và sự đồng nhất giữa các sơ đồ thiết kế. |

*Ghi chú:*
- Nếu ở bài nộp này sinh viên **hoàn toàn không sử dụng bất kỳ công cụ AI nào**, hãy ghi rõ `Không sử dụng công cụ AI` vào bảng.



### III. CAM KẾT VỀ LIÊM CHÍNH HỌC THUẬT

> **"Tôi xác nhận đã đọc, hiểu và chịu trách nhiệm về toàn bộ nội dung nộp."**

* **Chữ ký / Họ tên sinh viên:** Huỳnh Minh Trí  
* **MSSV:** 2374802010514
* **Ngày khai báo:** 06/10/2026


<br>
<hr style="border: 2px solid #2c3e50; border-radius: 5px;" />
<br>


# Khai báo sử dụng công cụ AI hỗ trợ

### II. BẢNG KHAI BÁO CHI TIẾT

| Hạng mục khai báo | Nội dung chi tiết |
| :--- | :--- |
| **1. Công cụ AI sử dụng** | Google Gemini. |
| **2. Mục đích sử dụng** | - Hỗ trợ thiết kế cấu trúc và hoàn thiện mã nguồn luồng ETL (Extract, Quality Check, Transform, Load) xử lý dữ liệu đơn hàng.<br>- Hỗ trợ viết Unit Test (`pytest`) và xử lý các lỗi phát sinh trong quá trình vận hành pipeline.<br>- Hỗ trợ hướng dẫn cấu trúc và quản lý tệp tin minh chứng cho báo cáo. |
| **3. Cách thức kiểm chứng** | - Tự chạy kiểm thử và xác thực toàn bộ mã nguồn trên môi trường thực tế (Terminal và SQLite).<br>- Rà soát thủ công các kết quả đầu ra (`staging_sales`, `dq_error_log`) để đảm bảo tính chính xác của dữ liệu.<br>- Đối chiếu chéo logic xử lý với các yêu cầu kỹ thuật của bài tập. |

*Ghi chú:*
- Nếu ở bài nộp này sinh viên **hoàn toàn không sử dụng bất kỳ công cụ AI nào**, hãy ghi rõ `Không sử dụng công cụ AI` vào bảng.

---

### III. CAM KẾT VỀ LIÊM CHÍNH HỌC THUẬT

> **"Tôi xác nhận đã đọc, hiểu và chịu trách nhiệm về toàn bộ nội dung nộp."**

- **Chữ ký / Họ tên sinh viên:** Huỳnh Minh Trí  
- **MSSV:** 2374802010514
- **Ngày khai báo:** 17/10/2026



<br>
<hr style="border: 2px solid #2c3e50; border-radius: 5px;" />
<br>




# Khai báo sử dụng công cụ AI hỗ trợ (Bài tập 2)

### I. BẢNG KHAI BÁO CHI TIẾT

| Công cụ AI | Dùng vào việc gì | Áp dụng ở tệp / hàm nào | Em đã kiểm chứng thế nào |
| :--- | :--- | :--- | :--- |
| **Google Gemini** | Hỗ trợ gợi ý mã nguồn nạp dữ liệu vào mô hình Star Schema từ bảng Staging. | `src/load/dwh_builder.py` (hàm `build_star_schema`) | Chạy thử pipeline và mở file `.db` bằng SQLite để xác nhận dữ liệu đổ vào đúng 3 bảng `Fact_Sales`, `Dim_Time`, `Dim_Customer` mà không bị nhân đôi[cite: 9]. |
| **Google Gemini** | Hỗ trợ cú pháp thư viện Streamlit và Matplotlib để vẽ biểu đồ doanh thu và SLA. | `src/dashboard.py` | Chạy lệnh `streamlit run` để kiểm tra thực tế trên trình duyệt, đảm bảo giao diện xử lý đúng dữ liệu và hiển thị đủ các đường cơ sở. |
| **Google Gemini** | Gợi ý cấu trúc viết Unit Test (pytest) cho các trường hợp kiểm tra giá trị biên và dữ liệu sai. | `tests/test_transform.py` | Đọc hiểu từng test case, tự chạy lệnh `pytest` trên Terminal và xác nhận toàn bộ 5/5 test đều PASS[cite: 9]. |
| **Google Gemini** | Hướng dẫn xử lý lỗi môi trường ảo (venv) trên Windows và gợi ý cấu trúc file tài liệu cấu hình. | `README.md`, `.env.example`, `docs/thay-doi-thiet-ke.md` | Đọc đối chiếu với yêu cầu của đề bài; tự clone source code ra một thư mục trống và chạy lại từ đầu theo đúng hướng dẫn trong README[cite: 9]. |

*Ghi chú:*
- Nếu ở bài nộp này sinh viên **hoàn toàn không sử dụng bất kỳ công cụ AI nào**, hãy ghi rõ `Không sử dụng công cụ AI` vào bảng.

---

### II. CAM KẾT VỀ LIÊM CHÍNH HỌC THUẬT

> **"Tôi xác nhận đã đọc, hiểu và chịu trách nhiệm về toàn bộ nội dung mã nguồn cũng như tài liệu đã nộp. Tôi có thể giải thích được các đoạn mã do AI hỗ trợ sinh ra nếu được giảng viên yêu cầu."**

- **Chữ ký / Họ tên sinh viên:** Huỳnh Minh Trí 
- **MSSV:** 2374802010514
- **Ngày khai báo:** 01/11/2026