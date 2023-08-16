
# Tupla        0         1    2      3         4                     5
miTupla = ("Mensaje 23", 7, 3.1415, True, [34, 54, 67], (8 , "mensaje tupla", False))
print(miTupla)


# La tupla no se puede modificar como una Lista


# Buscar en una tupla por el indice
print(miTupla[4])




# Crear sub-tuplas
# [inicio:fin]
# [inicio:fin:salto]
# Tupla        0         1    2      3         4                     5
miTupla = ("Mensaje 23", 7, 3.1415, True, [34, 54, 67], (8 , "mensaje tupla", False))

subTupla = miTupla[0:2]
print(subTupla)

subTupla = miTupla[1:]
print(subTupla)

subTupla = miTupla[:3]
print(subTupla)

subTupla = miTupla[0:100]
print(subTupla)

subTupla = miTupla[0:3:1]
print(subTupla)

subTupla = miTupla[:]
print(subTupla)


# Listas y Tuplas
valorA = ["Basico", "Intermedio", "Master"]
valorB = ("Ingles", "Frances", "Aleman")

generarTupla = tuple(valorA)
print(generarTupla)
print(type(generarTupla))

generarLista = list(valorB)
print(generarLista)
print(type(generarLista))





# Descomprimir / Desempaquetado
numerico = (10, 20, 30, 40)
primero, segundo, tercero, cuarto = numerico
print(primero, segundo, tercero, cuarto)

'''
    primero = numerico[0]
    segundo = numerico[1]
    tercero = numerico[2]
    cuarto = numerico[3]
'''

# * como prefijo significa que sera asignado como lista
numerico = (10, 20, 30, 40, 50, 60, 70)
primero, segundo, tercero, cuarto, *restante = numerico
print(primero, segundo, tercero, cuarto, restante)

# *_ significa omitir valores
primero, segundo, tercero, cuarto, *_ = numerico
print(primero, segundo, tercero, cuarto)


# *_ significa omitir valores
numerico = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
primero, segundo, tercero, cuarto, *restante , noveno, cien = numerico
print(primero, segundo, tercero, cuarto, restante , noveno, cien)





# Zip (Combinar valores)
lista = [1, 3, 5, 6]
tupla = ("Hola", "Mundo", True)

resultado = zip(tupla, lista) 
print(resultado)

resultado = tuple(resultado)
print(resultado)

