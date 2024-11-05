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
        
        # covariante, funciones necesarias de samples de columnas
        cov = np.cov(X.T)
        
        #Vectores Propios, valores Propios
        vectorespropios, valorespropios = np.linalg.eig(cov)
       
        #Vectores Propios v=[:, i] columna de vectores, interponiense para faciles calculos
        vectorespropios = vectorespropios.T
        
        # orden de vetores propios
        idxs = np.argsort(valorespropios)[::-1]
        valorespropios = valorespropios[idxs]
        vectorespropios = vectorespropios[idxs]
        
