
listaString = ["mensaje 1", "mensaje 2", "mensaje 3", "mensaje 4"]
indice = 0

while indice < len(listaString):
    print(listaString[indice])
    indice += 1
    if indice == 2:
        break
else:
    print("While finalizado!")




listaString = ["mensaje 1", "mensaje 2", "mensaje 3", "mensaje 4"]

for elemento in listaString:
    print(elemento)
    if indice == 2:
        break