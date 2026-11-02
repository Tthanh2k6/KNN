# K-Means Clustering and Choosing k with the Elbow Method

Course group project (Artificial Intelligence, Topic 2). The repository is named `KNN`, but the work is about **K-Means clustering**, not k-nearest neighbours.

<div align="center">
  <img src="https://raw.githubusercontent.com/Tthanh2k6/Portfolio/main/public/IMG/project-knn.png" alt="K-Means WCSS Elbow method and Silhouette Score" width="100%" />

  <br />

  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/scikit--learn-KMeans-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" alt="scikit-learn" />
    <img src="https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter" />
    <img src="https://img.shields.io/badge/Matplotlib_%26_Seaborn-Visualization-11557C?style=flat-square" alt="Matplotlib" />
  </p>
</div>

---

## Overview

A study of **K-Means clustering** and of **choosing the number of clusters `k`** with the **Within-Cluster Sum of Squares (WCSS) Elbow Method**, **Kneedle knee-point detection** and the **Silhouette Coefficient**, on public datasets (Mall_Customers, Iris) and synthetic ones (make_blobs, make_moons).

### What the notebooks do
1. **Data Standardization & EDA:** Feature scaling (StandardScaler) and exploratory distribution analysis across income and spending-score dimensions.
2. **WCSS Elbow & Kneedle:** Sweeps `k` from 1 to 10 and computes WCSS. On the scaled Iris data the notebook picks `k = 3` (WCSS 600.0 → 229.7 → 153.0, then a slower decline); the Mall Customers WCSS values for `k = 1..10` are printed in `02_elbow_method_analysis.ipynb`. `src/utils.py` implements Kneedle to pick the knee automatically.
3. **Ambiguous elbows:** Compares the WCSS curve with **Silhouette Scores** (`03_silhouette_vs_elbow.ipynb`, Mall Customers, `k = 2..10`) and tests non-convex clusters (make_moons) in `Test/Test_blobs.py`.
4. **Cluster plots:** Scatter plots of the clusters for several values of `k` (`src/visualization.py`).

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
- data/ — Datasets (CSV): original files in `data/Gốc/`, scaled versions in `data/Đã xử lí/`
- Test/ — Verification scripts
- docs/ — Group report and theory notes (Word documents)