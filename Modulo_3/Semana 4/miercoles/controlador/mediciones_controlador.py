from persistencia.ventas_reporsitorio import Vemtas_Repositorio
from datetime import datetime, timedelta

class Mediciones:    
    
    def obtener_ventas_dia(self): 
        return Vemtas_Repositorio().obtener_ventas_por_dia()        
    
    def obtener_total_genero(self):
        vr  = Vemtas_Repositorio().obtener_total_genero()
        values = [self.porcentaje(vr["female"],sum([vr["female"],vr["male"]])),self.porcentaje(vr["male"],sum([vr["male"],vr["female"]]))]
        key = vr["genders"]
        return {"key":key,"values":values}
    
    def obtener_total_ciudades(self):
        vr  = Vemtas_Repositorio().obtener_total_ciudades()
        key = vr["cities"]
        yangon = self.porcentaje(vr["Yangon"],sum([vr["Yangon"],vr["Mandalay"],vr["Naypyitaw"]]))
        mandalay = self.porcentaje(vr['Mandalay'],sum([vr["Yangon"],vr["Mandalay"],vr["Naypyitaw"]])),
        naypyitaw = self.porcentaje(vr["Naypyitaw"],sum([vr["Yangon"],vr["Yangon"],vr["Naypyitaw"]]))
        values = [ yangon  ,mandalay    ,naypyitaw         ]
        return {"key":key,"values":values}
        
    def porcentaje(self,numero,total):
        return 100 * float(numero) / float(total)