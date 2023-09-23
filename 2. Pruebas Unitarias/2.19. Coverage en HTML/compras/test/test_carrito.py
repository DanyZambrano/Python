import unittest
from compras.productos import Producto
from compras.carrito import Carrito


class ProductError(Exception):
    pass


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
        #self.assertFalse(self.item2.carrito_conItems(), "El Carrito tiene items ")

    # AsserNotIn (valida si un objeto existe en ...)
    def test_productosEnCarrito(self):
        self.item2.carrito_remover(self.auto)
        self.assertNotIn(self.auto, self.item2.productos)

    # AssertRaise (Levanta una excepcion)
    def test_productosError(self):
        #with self.assertRaises(ProductError):
        #    Producto("Motocicleta", 1000, 10.9)
        pass


    # Skip (Saltar una Prueba)
    # skipIf  (evalua si en True)
    # skipUnless (evalua si en False)
    # python3 -m unittest [nombre de archivo] -v

    def test_compra(self):
        self.assertGreater(20, 40)


    def test_compra2(self):
        self.assertGreater(20, 40)


    def test_compra3(self):
        self.assertGreater(20, 40)


