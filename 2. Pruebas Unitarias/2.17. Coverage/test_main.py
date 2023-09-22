import pytest

class TestSaludos():

    def test_saludo(self):
        assert "hola" == "hola", "Saludo no exitoso!"

    def test_saludo2(self):
        assert "hola" == "h0la", "Saludo2 no exitoso!"
    