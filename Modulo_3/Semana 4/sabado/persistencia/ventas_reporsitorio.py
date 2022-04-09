import csv
from datetime import datetime

class Vemtas_Repositorio:    
    path_file = "./data/ventas.csv"
    
    def obtener_ventas_por_dia(self):      
        values, dates = [] , []                                                    
        with open(self.path_file, "r") as csvfile:
            self.reader_variable = csv.reader(csvfile, delimiter=",")        
            for idx, val in enumerate(self.reader_variable):  
                if(idx > 0):
                    date_time_str = f'{(val[10])} {val[11]}'
                    fechahora = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
                    dates.append(fechahora)
                    values.append(float(val[13]))                
        return  {"key":dates,"values":values}    

    
    def obtener_total_columna(self,columna):      
        unique_keys =  list(self.obtener_valores_unicos(columna))
        totales_keys =  dict.fromkeys(self.obtener_valores_unicos(columna),0)
        values =  self.obtener_filas_por_columna(columna)
                                                         
        return  {"total_row":len(values),"unique_keys":unique_keys,"column_values":values,"totales_keys":totales_keys}      
        
    def obtener_valores_unicos(self,columna:int):
        result = set()
        with open(self.path_file, "r") as csvfile:
            reader_variable = csv.reader(csvfile, delimiter=",")
            next(reader_variable)
            result = set([*map(lambda x: x[columna], reader_variable)])
        return result
    
    def obtener_filas_por_columna(self,columna:int):        
        with open(self.path_file, "r") as csvfile:
            reader_variable = csv.reader(csvfile, delimiter=",")
            next(reader_variable)
            result = [*map(lambda x: x[columna], reader_variable)]
        return result