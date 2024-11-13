#Jonathan Hernandez 

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
               selft.n_componentes = vectorespropios[selft.n_componentes]
    def transform(self, X):
        #Datos de proyectos
        X = X - self.mean
        return np.dot(X, self.n_componentes.T)
    
#testing
if __name__ == "__main__":
    #importaciones
    import matplotlib.pyplot as plt
    from sklearn import datasets
    
    #datos = datasets. cargar_digitos()
    data = datasets.load_iris()
    X = data.data
    y = data.target
    
    # Project the data onto the 2 primary principal components
    pca = PCA(2)
    pca.fit(X)
    X_projected = pca.transform(X)

    print("Shape of X:", X.shape)
    print("Shape of transformed X:", X.shape)

    x1 = X_projected[:, 0]
    x2 = X_projected[:, 1]

    plt.scatter(
        x1, x2, c=y, edgecolor="none", alpha=0.8, cmap=plt.cm.get_cmap("viridis", 3)
    )

    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.colorbar()
    plt.show()
    
           
