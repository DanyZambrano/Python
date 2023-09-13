import unittest
from productos import Producto
from carrito import Carrito

class TestCarrito(unittest.TestCase):

    # --------------------------------------------------
    # Esto define acciones antes y luego de las pruebas


    # Se ejecuta antes de las pruebas (Inicializar Objetos)
    def setUp(self):
        self.item1 = Carrito()

        self.item2 = Carrito()
        self.nombre = "Renault"
        self.precio = 20000,0
        self.auto = Producto(self.nombre, self.precio)
        self.item2.carrito_agregar(self.auto)
        
    

    # Se ejecuta luego de las pruebas (Restablecer los objetos)
    def tearDown(self):
        pass

    # --------------------------------------------------


    def test_producto(self):
        nombre = "playstation 5"
        precio = 500
        item = Producto(nombre, precio)


    def test_carrito_vacio(self):
        self.assertTrue(self.item1.carrito_vacio(), "El Carrito tiene items ")

    def test_carrito_cantidad(self):
        self.assertTrue(self.item2.carrito_conItems(), "El Carrito No tiene items ")
        self.assertFalse(self.item2.carrito_conItems(), "El Carrito tiene items ")


if __name__ == '__main__':
    unittest.main()