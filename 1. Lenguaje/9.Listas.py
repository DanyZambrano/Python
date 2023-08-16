# Listas

# Genericas
miLista = [7, 3.1515, True, "Mensaje"]
print(miLista)


# Por tipo
listaEnteros = [1, 7, 4, 6, -3]
listaString = ["mensaje 1", "mensaje 2", "mensaje 3", "mensaje 4"]
listaFlotantes = [3.1416, 3.1415]
listaBooleanos = [True, True, False, (5>5), ("menaje1" == "mensaje2")]

print(listaEnteros)
print(listaString)
print(listaFlotantes)
print(listaBooleanos)



# Longitud de la lista
longitud = len(listaString)
print(longitud)




# Indices           0           1             2            3
listaString = ["mensaje 1", "mensaje 2", "mensaje 3", "mensaje 4"]
print(listaString[3])


# Indices           -4          -3             -2            -1
listaString = ["mensaje 1", "mensaje 2", "mensaje 3", "mensaje 4"]
print(listaString[-1])




# Modificar un elemento en la Lista
listaString = ["mensaje 1", "mensaje 2", "mensaje 3", "mensaje 4"]
listaString[3] = "Nuevo Mensaje"
print(listaString)




# Crear una Sub-Lista
# [inicio:fin]
# [inicio:fin:salto]
listaString = ["mensaje 1", "mensaje 2", "mensaje 3", "mensaje 4"]

miSubLista = listaString[0:2]
print(miSubLista)

miSubLista = listaString[1:]
print(miSubLista)

miSubLista = listaString[:3]
print(miSubLista)

miSubLista = listaString[0:100]
print(miSubLista)

miSubLista = listaString[0:3:1]
print(miSubLista)

miSubLista = listaString[:]
print(miSubLista)





# Agregar elementos a la Lista
listaString = ["mensaje 1", "mensaje 2", "mensaje 3", "mensaje 4"]

listaString.append('Mensaje 5')
print(listaString)

listaString.append('Mensaje 6')
print(listaString)

print(len(listaString))





listaString.insert(1, 'Mensaje nuevo')
print(listaString)


listaStringDos = ["mensaje 7", "mensaje 8", "mensaje 9", "mensaje 10"]
listaString.extend(listaStringDos)
print(listaString)
print(len(listaString))





# Eliminar elementos en la lista
listaString.remove("mensaje 8")
print(listaString)

del listaString[5]
print(listaString)


# Limpiar toda la lista
listaString.clear()
print("len: ", len(listaString))





# Ordenar una lista
listaNumeros = [7, 4, 6, -3, 1, 0]

listaNumeros.sort()
print(listaNumeros)


# Minimo y Maximo en la lista
print(min(listaNumeros))
print(max(listaNumeros))




# Buscar en una lista
listaNumeros = [7, 4, 6, -3, 1, 0]
seEncuentra = -3 in listaNumeros
print(seEncuentra)

seEncuentra = 2 not in listaNumeros
print(seEncuentra)


listaNumeros = [4, -6, 8, 23 ,100, 0]
indiceBusqueda = listaNumeros.index(-6)
print(indiceBusqueda)

