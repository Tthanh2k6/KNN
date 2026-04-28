def aggregate_wcss(all_wcss, method='mean'):
    """
    Tổng hợp ma trận WCSS (n_runs x len(k_range)) thành một vector đại diện.

    Tham số:
        all_wcss (np.ndarray): Đầu ra của run_kmeans_multiple_times(),
                               kích thước (n_runs, len(k_range)).
        method (str): Cách tổng hợp:
                      - 'mean'   : trung bình các lần chạy (mặc định, ổn định nhất)
                      - 'median' : trung vị (ít nhạy cảm với outlier)
                      - 'min'    : lấy giá trị nhỏ nhất (lần chạy tốt nhất)

    Trả về:
        wcss_agg (np.ndarray): Vector WCSS đã tổng hợp, kích thước (len(k_range),).

    Ví dụ:
        all_wcss = run_kmeans_multiple_times(X, range(1, 11), n_runs=10)
        wcss_mean = aggregate_wcss(all_wcss, method='mean')
    """
    all_wcss = np.array(all_wcss)

    if method == 'mean':
        return np.mean(all_wcss, axis=0)
    elif method == 'median':
        return np.median(all_wcss, axis=0)
    elif method == 'min':
        return np.min(all_wcss, axis=0)
    else:
        raise ValueError(f"method='{method}' không hợp lệ. Chọn: 'mean', 'median', 'min'.")

def find_knee_kneedle(k_range, wcss_agg, sensitivity=1.0):
    """
    Tìm điểm khuỷu tay (elbow/knee) từ vector WCSS đã tổng hợp
    bằng thuật toán Kneedle (Satopaa et al., 2011).

    Thuật toán:
        1. Chuẩn hóa (k, WCSS) về đoạn [0, 1] x [0, 1].
        2. Tính đường baseline nối điểm đầu và điểm cuối.
        3. Tính hiệu số: difference[i] = y_norm[i] - baseline[i].
        4. Điểm khuỷu là chỉ số i đầu tiên vượt ngưỡng T = max(difference) - S * step,
           trong đó S là sensitivity và step là bước chuẩn hóa trung bình.

    Tham số:
        k_range  (iterable) : Danh sách giá trị k đã dùng khi tính WCSS.
        wcss_agg (np.ndarray): Vector WCSS đại diện (đầu ra của aggregate_wcss).
        sensitivity (float) : Độ nhạy S >= 0.
                              - S nhỏ (0.5): chọn điểm khuỷu sớm hơn (k nhỏ hơn).
                              - S lớn (2.0): chọn điểm khuỷu muộn hơn (k lớn hơn).

    Trả về:
        knee_k (int): Giá trị k tối ưu theo Kneedle.

    Ví dụ:
        all_wcss  = run_kmeans_multiple_times(X, range(1, 11), n_runs=10)
        wcss_mean = aggregate_wcss(all_wcss, method='mean')
        k_opt     = find_knee_kneedle(range(1, 11), wcss_mean, sensitivity=1.0)
        print(f"K tối ưu: {k_opt}")
    """
    k_arr = np.array(list(k_range), dtype=float)
    wcss_arr = np.array(wcss_agg, dtype=float)
    
    # 1. Chuẩn hóa dữ liệu về khoảng [0, 1]
    x_norm = (k_arr - k_arr.min()) / (k_arr.max() - k_arr.min())
    y_norm = (wcss_arr - wcss_arr.min()) / (wcss_arr.max() - wcss_arr.min())
    
    # 2. Tính toán đường baseline và hiệu số (difference)
    baseline = 1 - x_norm 
    difference = y_norm - baseline 
    
    # 3. Xác định vùng tìm kiếm (giới hạn khi WCSS giảm 95% tổng thể)
    threshold_95 = wcss_arr.min() + 0.05 * (wcss_arr.max() - wcss_arr.min())
    search_range = np.where(wcss_arr >= threshold_95)[0]
    
    # 4. Tìm chỉ số điểm khuỷu tay (knee)
    if len(search_range) > 0:
        diff_subset = difference[search_range]
        knee_idx = search_range[np.argmin(diff_subset)] 
    else:
        knee_idx = np.argmin(difference)

    return int(k_arr[knee_idx])
