def nombreFuncion():
    #logica
    return

nombreFuncion()





# Defines la funcion y luego llamas la funcion para ejecutarla
# Una funcion debe ser Atomica (un solo proposito)

def sumatoria():
    valorA = int(input("Ingrese valorA: "))
    valorB = int(input("Ingrese valorB: "))
    valorC = int(input("Ingrese valorC: "))
    suma = valorA + valorB + valorC
    print(suma)


sumatoria()






# Funcion con Argumentos
def sumatoria(valorA, valorB, valorC):
    suma = valorA + valorB + valorC
    print(suma)


sumatoria(10, 20, 30)







# Funcion con Retorno de valor
def sumatoria(valorA, valorB, valorC):
    suma = valorA + valorB + valorC
    return suma


suma = sumatoria(10, 20, 30)
print("La sumatoria es: ", suma)








# Funcion con Retorno de valor
def sumatoria(valorA, valorB, valorC):
    return (valorA + valorB + valorC)


suma = sumatoria(10, 20, 30)
print("La sumatoria es: ", suma)







# Funcion con Retorno de valor tipo tupla
def sumatoria(valorA, valorB, valorC):
    return (valorA + valorB + valorC), "Aqui el resultado final", 0.0


suma = sumatoria(10, 20, 30)
print("La sumatoria es: ", suma)







# Funcion con Retorno de valor tipo tupla (desempaquetar)
def sumatoria(valorA, valorB, valorC):
    return (valorA + valorB + valorC), "Aqui el resultado final", 0.0


suma, mensaje, porcentaje = sumatoria(10, 20, 30)
print("Los datos son", suma, mensaje, porcentaje)







# Funcion con valores por defecto
# Deben estar a la derecha
# = debe estar pegado al valor por convencion
def sumatoria(valorA, valorB, valorC=40):
    return (valorA + valorB + valorC)


suma = sumatoria(10, 20)
print("La sumatoria es: ", suma)







# N cantidad de argumentos
# colocar *
# args por convencion
def average(*valores):
    return sum(valores) / len(valores)


data = average(10, 20, 50, 60, 70, 1000)
print("El average es: ", data)








# N cantidad de argumentos
# colocar *
# args por convencion
def aleatorio(valorA, valorB, *arg, valorC=2):
    print(arg)
    return ((valorA + valorB) + sum(arg)) / valorC


data = aleatorio(10, 20, 50, 60, 70, 1000)
print("El average es: ", data)








# Pasar diccionarios (key:value)
# **
def finales(**notas):
    print(notas)
    print(type(notas))


finales(dany=10, samuel=20, santiago=[10, 15, 20])








# combinacion de tuplas y diccionarios
def especial(*valores, **notas):
    print(valores)
    print(type(valores))

    print(notas)
    print(type(notas))


especial((10, 1.0, True, "Hola"), dany=10, samuel=20, santiago=[10, 15, 20])




