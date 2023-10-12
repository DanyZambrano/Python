lista = [2,1,3,4,5]
orden = sorted(lista)
print(orden)



lista = ["h", "c", "b", "a", "g"]
lista.sort()
print(lista)



lista = [4, 1, 2, 3]
lista.reverse()
print(lista)



lista = [1, 2, 3]
resultado = [3*x for x in lista]
print(resultado)



listA = [1, 2, 3]
listB = [5, 6, 7]
resultado = [a+b for a in listA for b in listB]
print(resultado)





listA = ['a', 'list', 'of', 'words']
listB = [s.upper() for s in listA]
listC = [s for s in listA if len(s) <=2]
listD = [s for s in listA if 'w' in s]
print('listA:',listA)
print('listB:',listB)
print('listC:',listC)
print('listD:',listD)




lista = [1, -2, 3, -5, 6, -7, 8]
positivo = [n for n in lista if n > 0]
negativo = [n for n in lista if n < 0]
print(positivo)
print(negativo)



lista    = [1, 2, 3, 4]
lista_cuadrado = [ n*n   for n in lista ]
lista_cubo   = [ n*n*n for n in lista ]
print('lista:   ',lista)
print('lista_cuadrado:',lista_cuadrado)
print('lista_cubo:  ',lista_cubo)



mensaje = ['te', 'gusta', 'Pyhton?']
print(" ".join(mensaje))






lista = [1, 2, "f", 2, 4, 2, 5, 7, "f"]
print(lista.count("f"), lista.count(2))




from collections import Counter

lista = ['a', 'b', 'a', 'b', 'c', 'a', 'd', 'e', 'f', 'b']
resultado = Counter(lista)
print(resultado)

