import pandas as pd 
   
data = pd.read_csv("ventas.csv") 
    
# eliminando columnas de valor nulo para evitar errores
data.dropna(inplace = True) 
   
# almacenar dtype antes de convertir
before = data.dtypes 
   
# convertir dtypes usando astype 
data["Total"]= data["Total"].astype(int) 
data["Precio por unidad"]= data["Precio por unidad"].astype(str) 
   
# almacenar dtype después de convertir
after = data.dtypes 
   
# impresión para comparar
print("ANTES DE LA CONVERSIÓN\n", before, "\n") 
print("DESPUÉS DE LA CONVERSIÓN\n", after, "\n") 
