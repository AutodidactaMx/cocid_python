# importing pandas module  
import pandas as pd  
     
# Hacer data frame  
df = pd.read_csv("./ventas.csv")  
   
ser = pd.Series(list("abcdef"), index=[49, 48, 47, 0, 1, 2]) 
data = ser.head(10)
print(data.loc[0]) 
