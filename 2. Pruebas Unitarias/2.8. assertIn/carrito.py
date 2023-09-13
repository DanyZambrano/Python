from productos import Producto

class Carrito:

    def __init__(self) -> None:
        self.__productos = list()

    def carrito_vacio(self) -> bool:
        return len(self.__productos) == 0
    
    def carrito_conItems(self) -> bool:
        return len(self.__productos) > 0
    
    def carrito_agregar(self, producto: Producto) -> None:
        self.__productos.append(producto)

    def carrito_remover(self, producto: Producto) -> None:
        self.__productos.remove(producto)

        

    # Este decorador convierte al metodo en un atributo
    # El copy, copia el objeto y evita su manipulacion sobre el original
    @property
    def productos(self):
        return self.__productos.copy()
