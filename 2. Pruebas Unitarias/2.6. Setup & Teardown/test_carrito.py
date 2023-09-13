import unittest
from productos import Producto

class TestCarrito(unittest.TestCase):

    # --------------------------------------------------
    # Esto define acciones antes y luego de las pruebas


    # Se ejecuta antes de las pruebas (Inicializar Objetos)
    def setUp(self):
        self.nombre = "Renault"
        self.precio = 20000,0
        self.auto = Producto(self.nombre, self.precio)
    

    # Se ejecuta luego de las pruebas (Restablecer los objetos)
    def tearDown(self):
        self.nombre = ""
        self.precio = 0,0

    # --------------------------------------------------





    # --------------------------------------------------
    # Metodos de Clases (setUp y tearDown)
    # Se empela para compartir informacion entre las pruebas unitarias


    # Se ejecuta antes de Todas las pruebas
    @classmethod
    def setUpClass(cls):
        print("Se ejecuta Antes de Todas las pruebas")
    

    # Se ejecuta luego de Todas las pruebas
    @classmethod
    def tearDownClass(cls):
        print("Se ejecuta Luego de Todas las pruebas")

    # --------------------------------------------------






    def test_producto(self):
        nombre = "playstation 5"
        precio = 500
        item = Producto(nombre, precio)

        self.assertEqual(item.nombre, nombre, "Error en el item Nombre")
        self.assertEqual(item.precio, precio, "Error en el item Precio")


    def test_precio(self):
        self.assertEqual(self.auto.nombre, self.nombre, "Error en el item Nombre")
        self.assertEqual(self.auto.precio, self.precio, "Error en el item Precio")


if __name__ == '__main__':
    unittest.main()