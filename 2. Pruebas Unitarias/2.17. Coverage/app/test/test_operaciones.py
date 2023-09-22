import pytest

class TestOperaciones():

    # Inicializar objetos
    def setup_method(self):
        self.valorA = 2
        self.valorB = 2

    # Restaurar objetos
    def teardown_method(self):
        self.valorA = 0
        self.valorB = 0


    def test_suma(self):
        assert self.valorA + self.valorB == 4, "Suma No Exitosa!"

    def test_resta(self):
        assert self.valorA - self.valorB == 0, "Resta No Exitosa!"