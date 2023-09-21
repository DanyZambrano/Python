import pytest

class TestOperaciones():

    # Inicializar objetos
    @classmethod
    def setup_class(cls):
        print("setup  - Metodo que se ejecuta ANTES de TODAS las pruebas")


    # Restaurar objetos
    @classmethod
    def teardown_class(cls):
        print("teardown  - Metodo que se ejecuta LUEGO de TODAS las pruebas")



    # Inicializar objetos
    def setup_method(self):
        print("setup  - Metodo que se ejecuta ANTES de CADA prueba")
        self.valorA = 2
        self.valorB = 2

    # Restaurar objetos
    def teardown_method(self):
        print("teardown  - Metodo que se ejecuta LUEGO de CADA prueba")
        self.valorA = 0
        self.valorB = 0



    def test_suma(self):
        assert self.valorA + self.valorB == 4, "Suma No Exitosa!"

    def test_resta(self):
        assert self.valorA - self.valorB == 1, "Resta No Exitosa!"