# Assert
# Es una palabra reservada para validar una condicion
# el resultado sera continuar la ejecucion o arrojar una excepcion 


assert "hola" == "hola"
print("Continuacion...")


assert "hola" == "h0la", " >>>> No hay Coincidencia!! <<<< "
print("Continuacion...")


try:
    assert "hola" == "h0la", ">>>> No hay Coincidencia!! <<<<"
except AssertionError as error:
    print("Error", error)
    


def sumatoria(valorA: int, valorB: int, valorC: int) -> int:
    '''
        Funcion para el calculo de la suma total de valores
        Los valores deben ser enteros positivos

        Argumentos: valores enteros

        Ejemplo:
            sumatoria(8, 2, 6)
    '''

    assert valorA >= 0 and valorB >= 0 and valorC >= 0, "Deben ser valores enteros positivos"

    suma = valorA + valorB + valorC
    return suma

sumatoria(10, -10, 20)