class VentaDepartamento:
    def __init__(self,tienda, departamento, ventas) -> None:
        self.tienda = tienda
        self.departamento = departamento
        self.ventas = ventas        

        
    def __repr__(self):
        return f'VentaDepartamento("{self.tienda}, {self.departamento}, {self.ventas}")\n'    
    
class VentaTienda:
    def __init__(self,tienda, ventas) -> None:
        self.tienda = tienda        
        self.ventas = ventas        
        
    def __repr__(self):
        return f'VentaDepartamento("{self.tienda},  {self.ventas}")\n'    
    