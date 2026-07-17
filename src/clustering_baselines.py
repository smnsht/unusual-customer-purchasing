import numpy as np
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score


class KMeansTrainingLoop:
    def __init__(self, X, k_values, random_state=42, sample_size=2000):
        if not isinstance(X, np.ndarray):
            raise ValueError("X must be a numpy ndarray")

        self.X = X
        self.k_values = k_values
        self.random_state = random_state
        self.sample_size = sample_size
        self.best_k = None
        self.best_silhouette = -1.0
        self.best_kmeans = None

        self.inertias = []
        self.silhouette_scores = []

    def train(self, eval_metric='euclidean'):
        # Reset state for repeated calls.
        self.best_k = None
        self.best_silhouette = -1.0
        self.best_kmeans = None
        self.inertias = []
        self.silhouette_scores = []

        n = self.X.shape[0]
        m = n if self.sample_size is None else min(self.sample_size, n)

        # Compute silhouette on a fixed sample for speed and fair comparison across k.
        rng = np.random.default_rng(self.random_state)
        sample_idx = rng.choice(n, size=m, replace=False)
        x_sample = self.X[sample_idx]

        for k in self.k_values:
            kmeans = KMeans(n_clusters=k, random_state=self.random_state, n_init="auto")
            kmeans.fit(self.X)

            inertia = kmeans.inertia_
            self.inertias.append(inertia)

            if k > 1:
                silhouette_avg = silhouette_score(x_sample, kmeans.predict(x_sample), metric=eval_metric)
                self.silhouette_scores.append(silhouette_avg)

                if silhouette_avg > self.best_silhouette:
                    self.best_silhouette = silhouette_avg
                    self.best_k = k
                    self.best_kmeans = kmeans
            else:
                self.silhouette_scores.append(None)

    def __str__(self):
        return (
            f"KMeansTrainingLoop(best_k={self.best_k}, "
            f"best_silhouette={self.best_silhouette:.4f}, "
            f"best_kmeans={self.best_kmeans})"
        )

class DBSCANEvaluation:
    def __init__(self, X, eps=None, min_samples=5, metric="euclidean"):
        if not isinstance(X, np.ndarray):
            raise ValueError("X must be a numpy ndarray.")

        self.X = X
        if eps is None:
            self.eps = np.sqrt(X.shape[1])
        else:
            self.eps = eps

        self.min_samples = min_samples
        self.metric = metric
        self._reset()

    def evaluate(self):
        # Reset state for repeated calls.
        self._reset()

        model = DBSCAN(eps=self.eps, min_samples=self.min_samples, metric=self.metric)
        labels = model.fit_predict(self.X)
        num_clusters = len(set(labels)) - (1 if -1 in labels else 0)

        cluster_labels = labels[labels != -1]
        if num_clusters >= 2 and len(cluster_labels) >= 2:
            non_noise_mask = labels != -1
            self.silhouette_avg_ = silhouette_score(
                self.X[non_noise_mask],
                labels[non_noise_mask],
                metric=self.metric,
            )

        self.num_noise_points_ = (labels == -1).sum()
        self.num_clusters_ = num_clusters
        self.labels_ = labels
        self.dbscan_model_ = model

    def _reset(self):
        self.labels_ = []
        self.num_clusters_ = 0
        self.num_noise_points_ = 0
        self.dbscan_model_ = None
        self.silhouette_avg_ = None

    def __str__(self):
        silhouette_info = (
            str(self.silhouette_avg_)
            if self.silhouette_avg_ is not None
            else "not computed."
        )

        return (
            f"DBSCAN Evaluation:\n"
            f"  Epsilon: {self.eps}\n"
            f"  Min Samples: {self.min_samples}\n"
            f"  Metric: {self.metric}\n"
            f"  Number of clusters: {self.num_clusters_}\n"
            f"  Number of noise points: {self.num_noise_points_}\n"
            f"  Silhouette score: {silhouette_info}\n"
        )

    def __repr__(self):
        return self.__str__()
