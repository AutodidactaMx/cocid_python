class MagnitudApocaliticaError(Exception):
    """Exception raised para errores de Magnitud.
    Attributes:        
        mensaje -- Explicacion del error
    """

    def __init__(self, mensaje="Magnitud Legendario o apocalíptico Nunca registrado."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class RangoError(Exception):
    """Exception raised para errores de Magnitud.
    Attributes:        
        mensaje -- Explicacion del error
    """

    def __init__(self, mensaje="El rango de inicio no puede ser mayor que el final"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)