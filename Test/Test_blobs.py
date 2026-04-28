import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_moons
from sklearn.preprocessing import StandardScaler

# Thêm đường dẫn gốc của project vào sys.path để import thư mục src
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
if project_dir not in sys.path:
    sys.path.append(project_dir)

from src.models import run_kmeans_multiple_times
import src.utils
# Inject numpy vào src.utils để tránh NameError mà không cần sửa file src/utils.py
src.utils.np = np
from src.utils import aggregate_wcss, find_knee_kneedle
from src.visualization import plot_elbow, plot_kmeans_subplots

def analyze_dataset(X, title, true_k=None):
    print(f"\n=== Phân tích dữ liệu: {title} ===")
    
    # Chuẩn hóa dữ liệu
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Thiết lập khoảng k để khảo sát
    k_range = range(1, 11)
    
    # 1. Chạy K-Means nhiều lần và tính WCSS
    print("Đang chạy K-Means...")
    all_wcss = run_kmeans_multiple_times(X_scaled, k_range, n_runs=10, init_method='k-means++')
    
    # 2. Tổng hợp WCSS bằng giá trị trung bình
    wcss_mean = aggregate_wcss(all_wcss, method='mean')
    
    # 3. Tìm điểm gãy (Elbow) bằng thuật toán Kneedle
    optimal_k = find_knee_kneedle(k_range, wcss_mean, sensitivity=1.0)
    print(f"Giá trị k tối ưu theo Kneedle: {optimal_k}")
    if true_k:
         print(f"Giá trị k thực tế: {true_k}")
         
    # 4. Trực quan hóa kết quả
    print("Vui lòng xem các đồ thị được hiển thị (đóng cửa sổ đồ thị để tiếp tục).")
    plot_elbow(k_range, wcss_mean, optimal_k)
    
    # Chọn một vài giá trị k để hiển thị
    k_values_to_plot = [2, 3, 4, optimal_k]
    # Loại bỏ các giá trị trùng lặp và sắp xếp
    k_values_to_plot = sorted(list(set(k_values_to_plot)))
    
    plot_kmeans_subplots(X_scaled, k_values_to_plot)
    print("-" * 50)

if __name__ == "__main__":
    # --- 1. Dữ liệu Blobs (Cụm hình cầu, rõ ràng) ---
    # Phù hợp với giả định của K-Means
    print("Tạo dữ liệu Blobs...")
    X_blobs, y_blobs = make_blobs(n_samples=500, centers=4, cluster_std=0.60, random_state=42)
    analyze_dataset(X_blobs, title="Dữ liệu Blobs (4 cụm rõ ràng)", true_k=4)
    
    # --- 2. Dữ liệu Moons (Cụm phi tuyến tính, hình bán nguyệt) ---
    # Phá vỡ giả định của K-Means
    print("Tạo dữ liệu Moons...")
    X_moons, y_moons = make_moons(n_samples=500, noise=0.05, random_state=42)
    analyze_dataset(X_moons, title="Dữ liệu Moons (2 cụm phi tuyến tính)", true_k=2)
