# Unsupervised Customer Segmentation & K-Means Elbow Optimization (KNN)

<div align="center">
  <img src="https://raw.githubusercontent.com/Tthanh2k6/Portfolio/main/public/IMG/project-knn.png" alt="K-Means WCSS Elbow Optimization, Silhouette Score & 2D PCA Clusters" width="100%" />

  <br />

  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/scikit--learn-KMeans_%26_PCA-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" alt="scikit-learn" />
    <img src="https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter" />
    <img src="https://img.shields.io/badge/Matplotlib_%26_Seaborn-Visualization-11557C?style=flat-square" alt="Matplotlib" />
  </p>
</div>

---

## 📊 Executive Overview

An empirical study and implementation of **K-Means Clustering** and **Optimal $ Selection** using the **Within-Cluster Sum of Squares (WCSS) Elbow Method**, **Kneedle knee-point detection**, **Silhouette Coefficient analysis**, and **2D PCA cluster projection** on real-world (Mall_Customers, Iris) and synthetic (make_blobs, make_moons) datasets.

### Key Engineering & Analytical Contributions
1. **Data Standardization & EDA:** Feature scaling (StandardScaler) and exploratory distribution analysis across income and spending-score dimensions.
2. **WCSS Inertia & Kneedle Inflection Detection:** Sweeps  \in [1..10]$, computes WCSS inertia, and pinpoints the mathematical elbow ( = 4$, WCSS = 73.6, Silhouette = 0.684).
3. **Ambiguous Elbow Mitigation:** Cross-validates ambiguous WCSS curves against **Silhouette Scores** and non-convex cluster geometries (make_moons).
4. **2D PCA Cluster Visualization:** Projects multi-dimensional customer segments onto principal components (PC1, PC2) with plotted centroids.

---

## 👥 Research Team (Artificial Intelligence Course — Topic 2)

| # | Member | GitHub | Core Responsibility |
| :---: | :--- | :--- | :--- |
| 1 | **Trần Trung Thành** | [@Tthanh2k6](https://github.com/Tthanh2k6) | Core K-Means implementation, Elbow sensitivity analysis & repository lead |
| 2 | **Trương Minh Trí** | [@EmmTee666](https://github.com/EmmTee666) | Inflection point math & Kneedle algorithm research |
| 3 | **Nguyễn Đăng Khoa** | [@dangkhoa126](https://github.com/dangkhoa126) | Ambiguous Elbow edge cases & mitigation strategies |
| 4 | **Nguyễn Hoàng Huy** | [@HoangHuy-DNS](https://github.com/HoangHuy-DNS) | Elbow curve & cluster scatter visualization |
| 5 | **Nguyễn Thái Thuận** | [@nguyenthaithuan2408](https://github.com/nguyenthaithuan2408) | Synthetic dataset generation (Blobs / Moons) & sensitivity testing |
| 6 | **Trương Gia Thuận** | [@p1n9v](https://github.com/p1n9v) | Geometric theory & mathematical formulation of WCSS |
| 7 | **Thân Nguyễn Dương Tuấn** | [@dtunabcd](https://github.com/dtunabcd) | Dataset curation (Mall Customers, Iris), EDA & preprocessing |
| 8 | **Nguyễn Việt Anh Khôi** | [@NguyenVietAnhKhoi](https://github.com/NguyenVietAnhKhoi) | Silhouette Score implementation & cross-comparison |
| 9 | **Anh Khôi** | [@browseK](https://github.com/browseK) | WCSS loop benchmarking & Q&A preparation |

---

## 📂 Repository Structure

- src/ — Python clustering and evaluation modules
- NoteBook/ — Interactive Jupyter Notebooks (.ipynb) with step-by-step derivations and plots
- data/ — Benchmark datasets (CSV, Excel)
- Test/ — Verification scripts
- docs/ — Presentation slides and technical report