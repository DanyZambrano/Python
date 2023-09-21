import pytest


class TestSaludos():

    def test_saludo(self):
        assert "hola" == "hola", "Saludo no exitoso!"

    def test_saludo2(self):
        assert "h0la" == "h0la", "Saludo2 no exitoso!"



class TestOperaciones():

    disponible = True

    def test_suma(self):
        assert 2 + 2 == 4, "Suma No Exitosa!"

    @pytest.mark.skip
    def test_resta(self):
        assert 2 - 2 == 0, "Resta No Exitosa!"

    @pytest.mark.skip(reason="Saltamos la prueba (test_restaDoble) por que no la entiendo!")
    def test_restaDoble(self):
        assert 2 - 2 == 0, "Resta No Exitosa!"

    @pytest.mark.skipif(disponible, reason="Saltamos la prueba (test_restaTriple) por que no la entiendo!")
    def test_restaTriple(self):
        assert 2 - 2 == 0, "Resta No Exitosa!"