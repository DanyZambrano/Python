class Producto:
    
    def __init__(self, nombre: str, precio: float, descuento: float = 0.0):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento
