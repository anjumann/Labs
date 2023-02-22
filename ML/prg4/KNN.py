import numpy as np
from collections import Counter

def euclidean_distance(x1,x2):
    return np.sqrt(np.sum((x1-x2)**2))

class k_nearest_neighbors:
    def __init__(self,k):
        self.k = k
    
    def knn_fit(self, X_train, Y_train):
        self.X_train = X_train
        self.Y_train = Y_train
    
    def knn_predict(self, X):
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)
    
    def _predict(self, x):
        distances = [euclidean_distance(x,x_train) for x_train in self.X_train]
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.Y_train[i] for i in k_indices]
        majority_vote = Counter(k_nearest_labels).most_common(1)
        return majority_vote[0][0]