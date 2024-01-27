# Una Matriz es un array de valores de dos dimensiones
# Ordenados por Filas y Columnas

vector = ["5", "2", "6"]
matriz = [ ["a","b","c"], ["d","e","f"] ]

'''
    a  b  c
    d  e  f
    h  i  j
'''

X = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
resultado = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in range(len(X)):
	for column in range(len(X[0])):
		resultado[row][column] = X[row][column] + Y[row][column]

for item in resultado:
	print(item)


