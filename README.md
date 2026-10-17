# Kho dữ liệu bán hàng và báo cáo doanh thu

**Sinh viên:** Huỳnh Minh Trí - MSSV
**Học phần:** Chuyên đề Tốt nghiệp 1, HK1 2026-2027
**Track:** DA
**Luồng nghiệp vụ:** L6 - Kho dữ liệu bán hàng và báo cáo doanh thu

## 1. Mục tiêu
Hệ thống giải quyết bài toán tổng hợp dữ liệu doanh thu thủ công bằng cách trích xuất, làm sạch dữ liệu từ 24 cửa hàng và xây dựng kho dữ liệu tập trung phục vụ ban giám đốc.

## 2. Yêu cầu môi trường (Dành cho Track DA)
*   **Ngôn ngữ:** Python 3.10+
*   **Thư viện cốt lõi:** `pandas` (xử lý dữ liệu in-memory), `pytest` (viết Unit Test).
*   **Cơ sở dữ liệu cục bộ:** SQLite hoặc DuckDB (phục vụ lưu trữ mô hình Star Schema nội bộ).
*   **Công cụ quản lý môi trường:** `venv`.

## 6. Trạng thái tiến độ hiện tại
*   **Trạng thái:** Đang thực hiện **Sprint 1 (Buổi 08)** - Hiện thực hóa module cốt lõi.
*   **Tiến độ:** 
    *   [x] Hoàn thành Đặc tả yêu cầu và Thiết kế kiến trúc (BT1).
    *   [x] Khắc phục các lỗi thiết kế theo feedback giảng viên (`docs/thay-doi-thiet-ke.md`).
    *   [ ] Dựng cấu trúc thư mục tách lớp `src/` (extract, transform, quality, load).
    *   [ ] Viết script pipeline ETL chạy bằng 1 lệnh.