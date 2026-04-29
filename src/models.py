from sklearn.cluster import KMeans
import numpy as np

def run_kmeans_multiple_times(X, k_range, n_runs=5, init_method='k-means++'):
    """
    Tham số:
        X (array-like): Dữ liệu đầu vào (đã được làm sạch và chuẩn hóa).
        k_range (iterable): Khoảng giá trị của K (số cụm) cần khảo sát (vd: range(1, 11)).
        n_runs (int): Số lần chạy lặp lại cho mỗi giá trị K.
        init_method (str): Phương pháp khởi tạo tâm cụm ('random' hoặc 'k-means++').
        
    Trả về:
        all_wcss (numpy array): Ma trận chứa giá trị WCSS. Kích thước (n_runs, len(k_range)).
                                Mỗi hàng là kết quả WCSS của một lần chạy toàn bộ k_range.
    """
    all_wcss = []
    
    for run in range(n_runs):
        wcss_run = []        
        # Lặp qua từng giá trị K
        for k in k_range:
            # Set n_init=1 để ép K-Means chỉ chạy 1 lần duy nhất cho mỗi model,
            # giúp ta quan sát rõ sự biến động do khởi tạo ngẫu nhiên gây ra.
            # random_state=None để mỗi lần gọi là một lần khởi tạo tâm ngẫu nhiên hoàn toàn.
            kmeans = KMeans(n_clusters=k, init=init_method, n_init=1, random_state=None)
            kmeans.fit(X)
            wcss_run.append(kmeans.inertia_)
            
        all_wcss.append(wcss_run)
        
    return np.array(all_wcss)

import pandas as pd
from sklearn.cluster import KMeans
 
 
def tinh_wcss(X, ten_dataset="Dataset"):
    """
    Chạy vòng lặp K=1→10, tính WCSS cho từng K.
 
    Tham số:
        X            : numpy array — dữ liệu đã StandardScaler (từ TV4)
        ten_dataset  : string      — tên dataset để in ra màn hình
 
    Trả về:
        wcss : list gồm 10 giá trị WCSS tương ứng K=1..10
    """
    print(f"\n{'='*45}")
    print(f"  {ten_dataset}")
    print(f"{'='*45}")
 
    wcss = []
 
    for k in range(1, 11):
        kmeans = KMeans(
            n_clusters  = k,
            init        = 'k-means++',
            n_init      = 10,
            max_iter    = 300,
            random_state= 42
        )
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)   # inertia_ = WCSS
        print(f"  K = {k:2d}  →  WCSS = {kmeans.inertia_:.4f}")
 
    return wcss
