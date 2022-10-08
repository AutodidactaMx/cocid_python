class VentasSemanales:

    def __init__(self, tienda, departamento, fecha, ventasSemanales, esVacaciones) -> None:
        self.tienda = tienda
        self.departamento = departamento
        self.fecha = fecha
        self.ventasSemanales = ventasSemanales
        self.esVacaciones = esVacaciones

    def __repr__(self):
        return f"{self.tienda}, {self.departamento}, {self.fecha}, {self.ventasSemanales}, {self.esVacaciones}"
    
    
    