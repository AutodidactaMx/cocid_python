from persistencia.ventas_reporsitorio import Ventas_Repositorio
from datetime import datetime, timedelta
import util.generic as utl
import util.constant as const

class Mediciones:    
    
    def obtener_ventas_dia(self): 
        return Ventas_Repositorio().obtener_ventas_por_dia()        
    
    def obtener_total_columna(self, columna):
        vr  = Ventas_Repositorio().obtener_total_columna(columna)
        values = []           
        key = vr["unique_keys"]
        tota_row = vr["total_row"]
        totales_keys = vr["totales_keys"]    
        column_values = vr["column_values"]  
        
        for value in column_values:   
            for column_key in totales_keys.keys():                
                if(column_key == value) :
                    totales_keys[column_key]+=1    
        
        for value in totales_keys.keys(): 
              values.append(utl.porcentaje(totales_keys[value] , tota_row))
        
        return {"key":key,"values":values}
    
    def obtener_total_genero(self):
        return self.obtener_total_columna(const.GENERO)            
    
    def obtener_total_ciudades(self):
        return self.obtener_total_columna(const.CIUDADES)            
    
    def obtener_total_tipo_cliente(self):
        return self.obtener_total_columna(const.TIPO_CLIENTE)            
