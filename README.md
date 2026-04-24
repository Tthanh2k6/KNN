Project_KMeans_Elbow/
│
├── data/                              # Lưu trữ dữ liệu (Thành viên 4 quản lý)
│   ├── Gốc/                           # Dữ liệu gốc (Mall_Customers.csv, Iris.csv...)
│   └── Đã xử lí/                      # Dữ liệu sau khi đã chuẩn hóa (StandardScaler)
│
├── notebooks/                         # File Jupyter Notebook để thử nghiệm
│   ├── 01_eda_preprocessing.ipynb     # Phần của TV4
│   ├── 02_elbow_method_analysis.ipynb # Phần của TV5, TV6, TV9
│   └── 03_silhouette_vs_elbow.ipynb   # Phần của TV3
│
├── src/                               # Mã nguồn Python (dạng file .py)
│   ├── __init__.py
│   ├── models.py                      # Chứa hàm chạy K-means (TV5, TV9)
│   ├── visualization.py               # Hàm vẽ đồ thị Elbow/Silhouette (TV6)
│   └── utils.py                       # Các hàm bổ trợ (tính WCSS, Kneedle - TV2)
│
├── docs/                              # Tài liệu nghiên cứu (Thành viên 1, 2, 7)
│   ├── theory/                        # Bài viết về WCSS, Kneedle, Elbow
│   └── reports/                       # File báo cáo cuối cùng (.pdf, .docx)
│
├── tests/                             # Test dữ liệu giả lập (Thành viên 8)
    └── test_blobs.py