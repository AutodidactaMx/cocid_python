class VentasModel:
    def __init__(self, id, descuento, total,propina,modo_pago,fecha_hora_venta) -> None:
        self.id = id
        self.descuento = descuento
        self.total = total
        self.propina = propina
        self.modo_pago = modo_pago
        self.fecha_hora_venta = fecha_hora_venta
    