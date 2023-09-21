import pytest

class TestSaludos():

    def test_saludo(self):
        assert "hola" == "hola", "Saludo no exitoso!"

    def test_saludo2(self):
        assert "h0la" == "h0la", "Saludo2 no exitoso!"
    