import csv
from datetime import datetime, timedelta

class Vemtas_Repositorio:    
            
    def obtener_ventas_por_dia(self):      
        dates = []
        values = []
        with open("./data/ventas.csv", "r") as csvfile:
            self.reader_variable = csv.reader(csvfile, delimiter=",")        
            for idx, val in enumerate(self.reader_variable):  
                if(idx >0  ):
                    date_time_str = f'{(val[10])} {val[11]}'
                    fechahora = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
                    dates.append(fechahora)
                    values.append(float(val[13]))                
        return  {"key":dates,"values":values}    

    def obtener_total_genero(self):      
        genders = ["Femenino","Masculino"]        
        male , female = 0, 0
        with open("./data/ventas.csv", "r") as csvfile:
            self.reader_variable = csv.reader(csvfile, delimiter=",")            
            for idx, val in enumerate(self.reader_variable):  
                if(idx >0):
                    gender = (val[4])
                    if(gender == "Male") :
                        male+=1
                    if(gender == "Female") :
                        female+=1                                      

        return  {"genders":genders,"male":male,"female":female}
    
    def obtener_total_ciudades(self):      
        cities = ["Yangon","Mandalay","Naypyitaw"]        
        Yangon ,Mandalay ,Naypyitaw = 0,0,0
        with open("./data/ventas.csv", "r") as csvfile:
            self.reader_variable = csv.reader(csvfile, delimiter=",")        
            for idx, val in enumerate(self.reader_variable):  
                if(idx >0):
                    city = (val[2])
                    if(city == "Yangon") :
                        Yangon+=1
                    if(city == "Mandalay") :
                        Mandalay+=1
                    if(city == "Naypyitaw") :
                        Naypyitaw+=1
            
        return  {"cities":cities,"Yangon":Yangon,"Naypyitaw":Naypyitaw,"Mandalay":Mandalay}
    
    def porcentaje(numero,total):
        return 100 * float(numero) / float(total)