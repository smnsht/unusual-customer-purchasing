import numpy as np
import matplotlib.pyplot as plt

PLOT_STYLES = {
    "silhouette": {"color": "#1f77b4", "marker": "o"},
    "noise": {"color": "#ff7f0e", "marker": "s"},
    "clusters": {"color": "#2ca02c", "marker": "^"},
}


def plot_eps_metrics(estimator):
    plt.figure(figsize=(10, 5))
    plt.plot(
        estimator.eps_,
        estimator.silhouette_avg_,
        label="Silhouette avg",
        **PLOT_STYLES["silhouette"],
    )
    plt.plot(
        estimator.eps_,
        estimator.num_clusters_,
        label="Num clusters",
        drawstyle="steps-mid",
        **PLOT_STYLES["clusters"],
    )
    plt.plot(
        estimator.eps_,
        np.log(estimator.num_noise_points_),
        label="Log of Num noise points",
        **PLOT_STYLES["noise"],
    )
    plt.xlabel("eps")
    plt.ylabel("value")
    plt.title(
        f"DBSCAN metrics vs eps (min_samples={estimator.min_samples}, {estimator.metric} metric)"
    )
    plt.legend()
    plt.show()
