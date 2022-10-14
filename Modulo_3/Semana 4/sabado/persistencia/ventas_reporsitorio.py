import csv
from datetime import datetime
import util.constant as const
class Ventas_Repositorio:    
    
    def obtener_ventas_por_dia(self):      
        values, dates = [] , []                                                    
        with open(const.PATH_FILE, "r") as csvfile:
            reader_variable = csv.reader(csvfile, delimiter=",")        
            next(reader_variable)
            for val in reader_variable:
                date_time_str = f'{(val[const.FECHA])} {val[const.HORA]}'
                fechahora = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
                dates.append(fechahora)
                values.append(float(val[const.TOTA_VENTAS]))                
        return  {"key":dates,"values":values}    
    
    def obtener_total_columna(self,columna:int):      
        unique_keys =  list(self.obtener_valores_unicos(columna))
        totales_keys =  dict.fromkeys(self.obtener_valores_unicos(columna),0)
        values =  self.obtener_filas_por_columna(columna)
                                                         
        return  {"total_row":len(values),"unique_keys":unique_keys,"column_values":values,"totales_keys":totales_keys}      
    
    def obtener_valores_unicos(self,columna:int=4):               
        return set(self.obtener_filas_por_columna(columna))        
    
    def obtener_filas_por_columna(self,columna:int):        
        with open(const.PATH_FILE, "r") as csvfile:
            reader_variable = csv.reader(csvfile, delimiter=",")
            next(reader_variable)
            result = [*map(lambda x: x[columna], reader_variable)]
        return result