
class Calculo():

    def sumatoria(valorA: int, valorB: int, valorC: int) -> int:
        '''
            Funcion para el calculo de la suma total de valores
            Los valores deben ser enteros positivos

            Argumentos: valores enteros

            Ejemplo:
                sumatoria(8, 2, 6)
        '''
        suma = valorA + valorB + valorC
        return suma
    
    
matematica = Calculo()
matematica.sumatoria(10, 20, 30)