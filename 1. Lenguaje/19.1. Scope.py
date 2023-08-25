
# Funcion y su scope

valorC = 15                      # variable global
def sumatoria(valorA, valorB):
    #valorC = 1                   # variable local
    suma = valorA + valorB + valorC
    return suma

print("valorC: ", valorC)   

suma = sumatoria(10, 20)
print("La sumatoria es: ", suma)




