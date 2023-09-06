

# Documentar una Funcion, metodo, clases, modulos es importante para las pruebas
# usar __doc__
def sumatoria(valorA, valorB, valorC):

    '''
        Funcion para el calculo de la suma de valores

        Argumentos:
        valorA
        valorB
        valorC
        
        Implementa esto en tu codigo

        Ejemplo:
            sumatoria(8, 2, 6)
    '''
    suma = valorA + valorB + valorC
    print(suma)


sumatoria(10, 20, 30)
#print(sumatoria.__doc__)
print(help(sumatoria))