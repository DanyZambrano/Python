import pytest

class TestSaludos():

    def test_saludo(self):
        assert "hola" == "hola", "Saludo no exitoso!"

    def test_saludo2(self):
        assert "hola" == "h0la", "Saludo2 no exitoso!"




class TestOperaciones():

    def test_suma(self):
        assert 2 + 2 == 4, "Suma No Exitosa!"

    def test_resta(self):
        assert 2 - 2 == 1, "Resta No Exitosa!"