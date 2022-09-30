class SalarioFueraRangoError(Exception):
    """Exception raised para errores de salario.

    Attributes:        
        mensaje -- Explicacion del error
    """

    def __init__(self, mensaje="Salalario no esta dentro del rango"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
