# [Môn Trí Tuệ Nhân Tạo] - Chủ đề 2: Ảnh hưởng của số cụm K (Elbow Method)

Đây là dự án lập trình và phân tích thực nghiệm cho bài tập nhóm môn Trí tuệ nhân tạo. Dự án tập trung vào việc nghiên cứu thuật toán phân cụm (Clustering) và cách tối ưu hóa tham số K thông qua phương pháp Elbow.

## 👥 Thông tin nhóm thực hiện

Dự án được phân công cụ thể cho 9 đầu việc, thực hiện bởi các thành viên:

| STT | Thành viên | GitHub | Phụ trách chính |
| :---: | :--- | :--- | :--- |
| 1 | **Trần Trung Thành** | [@Tthanh2k6](https://github.com/Tthanh2k6) | Code K-Means, kiểm tra biến động Elbow & Quản lý source code |
| 2 | **Trương Minh Trí** | [@EmmTee666](https://github.com/EmmTee666) | Giải thích "điểm gãy" & nghiên cứu thuật toán Kneedle |
| 3 | **Nguyễn Đăng Khoa** | [@dangkhoa126](https://github.com/dangkhoa126) | Phân tích các trường hợp Elbow mờ & đề xuất giải pháp |
| 4 | **Nguyễn Hoàng Huy** | [@HoangHuy-DNS](https://github.com/HoangHuy-DNS) | Vẽ đồ thị Elbow & trực quan hóa kết quả phân cụm |
| 5 | **Nguyễn Thái Thuận** | [@nguyenthaithuan2408](https://github.com/nguyenthaithuan2408) | Tạo dữ liệu giả lập (Blobs/Moons) kiểm tra độ nhạy Elbow |
| 6 | **Trương Gia Thuận** | [@p1n9v](https://github.com/p1n9v) | Nghiên cứu lý thuyết & ý nghĩa hình học của WCSS |
| 7 | **Thân Nguyễn Dương Tuấn**| *(Chưa có)* | Thu thập data (Mall Customers, Iris), EDA & Tiền xử lý |
| 8 | **Nguyễn Viết Anh Khôi** | *(Chưa có)* | Nghiên cứu & lập trình đối chiếu Silhouette Score |
| 9 | **Anh Khôi** | [@browseK](https://github.com/browseK) | Lập trình vòng lặp tính WCSS & Chuẩn bị Q&A |

## 📝 Mô tả chủ đề
**Chủ đề 2:** Phân tích ảnh hưởng của số cụm $K$ đối với thuật toán phân cụm và triển khai **Phương pháp khuỷu tay (Elbow Method)** để tìm giá trị $K$ tối ưu.

### Nội dung thực hiện:
1. **Tiền xử lý dữ liệu:** Làm sạch và chuẩn hóa dữ liệu đầu vào.
2. **Triển khai thuật toán:** Sử dụng K-Means Clustering để phân nhóm dữ liệu.
3. **Phân tích Elbow:** Tính toán *Sum of Squared Errors (SSE)* hoặc *Inertia* cho các giá trị $K$ khác nhau.
4. **Trực quan hóa:** Vẽ biểu đồ để xác định điểm "khuỷu tay" - nơi mà việc tăng thêm cụm không mang lại nhiều giá trị tối ưu cho mô hình.


## 📁 Cấu trúc Repository
- `src/`: Mã nguồn Python xử lý thuật toán.
- `data/`: Các tập dữ liệu mẫu dùng cho bài thuyết trình (CSV, Excel).
- `NoteBook/`: Chứa file `.ipynb` trình bày chi tiết quá trình chạy code, vẽ biểu đồ và giải thích kết quả.
- `docs/`: Tài liệu thuyết trình và file Word mô tả chi tiết 20 chủ đề.
- `Test/`: Các đoạn mã kiểm tra tính đúng đắn của thuật toán.

## 🛠 Yêu cầu hệ thống
Dự án sử dụng các thư viện phổ biến trong học máy:
- `scikit-learn`: Triển khai mô hình K-Means.
- `matplotlib` & `seaborn`: Trực quan hóa biểu đồ Elbow.
- `pandas` & `numpy`: Xử lý cấu trúc dữ liệu.

## 🚀 Cách chạy dự án
1. Mở file trong thư mục `NoteBook/` bằng **Google Colab** hoặc **Jupyter Notebook**.
2. Đảm bảo các file dữ liệu trong thư mục `data/` đã được tải lên đúng đường dẫn.
3. Chạy từng cell để xem kết quả phân cụm và biểu đồ phân tích số K.

---
*Dự án đang trong quá trình hoàn thiện (Work in Progress).*
