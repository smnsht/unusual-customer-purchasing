import numpy as np
from sklearn.cluster import KMeans
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
