Phần trực quan hóa K-Means (TV6)



Trong phần này, em thực hiện trực quan hóa kết quả phân cụm bằng phương pháp Elbow và biểu đồ so sánh.



Đầu tiên, phương pháp Elbow được sử dụng để xác định số cụm tối ưu (K). Từ đồ thị, giá trị WCSS giảm mạnh khi K tăng từ 1 đến 4, sau đó giảm chậm lại. Do đó, K = 4 được chọn là số cụm tối ưu.



Tiếp theo, em vẽ biểu đồ phân cụm với các giá trị K khác nhau (K = 2, 3, 4, 5). Kết quả cho thấy khi K = 4, các cụm được phân tách rõ ràng nhất. Khi K = 5, dữ liệu bị chia nhỏ không cần thiết, thể hiện hiện tượng overfitting.

