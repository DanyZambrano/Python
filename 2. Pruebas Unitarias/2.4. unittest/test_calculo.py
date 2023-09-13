
# Es una libreria Nativa de Python
# no debe existir una archivo que se llame unittest
# Las pruebas las colocamos en un archivo aparte de main

import unittest

class TestCalculo(unittest.TestCase):

    # Test #1
    def test_sumatoria(self) -> int:
        valorA = 10
        valorB = 10
        valorC = 60

        suma = valorA + valorB + valorC
        self.assertEqual(suma, 50)
        return suma
    
    
    # Test #2
    def test_restatoria(self) -> int:
        valorA = 60
        valorB = 10
        valorC = 10

        resta = valorA - valorB - valorC
        self.assertEqual(resta, 40)
        return resta
    


if __name__ == '__main__':
    unittest.main()