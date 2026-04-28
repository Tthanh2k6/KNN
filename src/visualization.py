import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def plot_elbow(k_range, wcss, optimal_k):
    plt.figure(figsize=(6,4))
    plt.plot(k_range, wcss, marker='o')
    plt.scatter(optimal_k, wcss[optimal_k-1], color='red', s=120)
    plt.title("Elbow Method")
    plt.xlabel("K")
    plt.ylabel("WCSS")
    plt.grid(True)
    plt.show()


def plot_kmeans_subplots(X, k_values):
    plt.figure(figsize=(12,8))

    for i, k in enumerate(k_values):
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(X)
        centers = kmeans.cluster_centers_

        plt.subplot(2,2,i+1)
        plt.scatter(X[:,0], X[:,1], c=labels, cmap='viridis')
        plt.scatter(centers[:,0], centers[:,1], c='red', s=200, marker='X')
        plt.title(f"K = {k}")

    plt.tight_layout()
    plt.show()