import numpy as np

class PCA:
    def __init__(selft, n_componentes):
        selft.n_componentes = n_componentes
        selft.n_componentes = None
        selft.mean = None
       
    def fit(selft, X):
        #men centrado
        selft.mean = np.mean(X, axis=0)
        X=X - selft.mean
