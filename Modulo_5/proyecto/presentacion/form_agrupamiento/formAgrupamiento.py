import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from presentacion.form_agrupamiento.formAgrupamiento_designer import FormAgrupamientoDesigner
sns.set()

class FormAgrupamiento(FormAgrupamientoDesigner):            
      
    def __init__(self, df):  
        super().__init__() 
        self.df = df
        self.initialize_component()                   
        self.inicio() 
        self.agrupado() 
        self.codo()  

    def codo(self):
        clientes = self.df[['Precio','edad_compra']]
        escalador = MinMaxScaler().fit(clientes.values)
        clientes = pd.DataFrame(escalador.transform(clientes.values),columns=["Precio", "edad_compra"])
        inercias = []
        for k in range(2, 10):
          kmeans = KMeans(n_clusters=k).fit(clientes.values)    
          inercias.append(kmeans.inertia_)
        
        axes = self.figure_codo.subplots()  
        axes.scatter(range(2, 10), inercias, marker="o", s=180, color="purple")
        axes.set_title("Codo", fontsize=20)        
        plt.show()   

    def agrupado(self):                
        clientes = self.df[['Precio','edad_compra']]
        escalador = MinMaxScaler().fit(clientes.values)
        clientes = pd.DataFrame(escalador.transform(clientes.values),columns=["Precio", "edad_compra"])

        kmeans = KMeans(n_clusters=3).fit(clientes.values)

        clientes["cluster"] = kmeans.labels_        
        colores = ["red", "blue", "orange", "black", "purple", "brown", "pink"]
        axes = self.figure_barra_edades.subplots()        
        for cluster in range(kmeans.n_clusters):
            axes.scatter(clientes[clientes["cluster"] == cluster]["Precio"],
                        clientes[clientes["cluster"] == cluster]["edad_compra"],
                        marker="o", s=80, color=colores[cluster], alpha=0.5)
            
            axes.scatter(kmeans.cluster_centers_[cluster][0], 
                        kmeans.cluster_centers_[cluster][1], 
                        marker="P", s=180, color=colores[cluster])
        axes.set_title("Agrupados", fontsize=20)
        axes.set_xlabel("Precio de bienes raices", fontsize=15)
        axes.set_ylabel("Edad de compra", fontsize=15)        
        axes.set_xlim(-0.1, 1.1)
        axes.set_ylim(-0.1, 1.1) 
        plt.show()     
    
    def inicio(self):                
        clientes = self.df[['Precio','edad_compra']]                
        axes = self.figure_dispersion.subplots()  
        axes.set_title("Original", fontsize=20)
        clientes.plot.scatter(x='Precio', y='edad_compra', ax=axes)
        plt.show() 