import unittest
from productos import Producto

class TestCarrito(unittest.TestCase):

    def test_producto(self):
        nombre = "playstation 5"
        precio = 500
        item = Producto(nombre, precio)

        self.assertEqual(item.nombre, nombre, "Error en el item Nombre")
        self.assertEqual(item.precio, precio, "Error en el item Precio")


if __name__ == '__main__':
    unittest.main()