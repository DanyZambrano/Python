
# Funcion y su scope

valorC = 15                      # variable global
def sumatoria(valorA, valorB):
    #valorC = 1                   # variable local
    suma = valorA + valorB + valorC
    return suma

print("valorC: ", valorC)   

suma = sumatoria(10, 20)
print("La sumatoria es: ", suma)








# Funciones Anidadas
def master():

    def operacionA():
        print("Operacion A")

    def operacionB():
        print("Operacion B")

    
    operacionA()
    operacionB()
    

master()








# Funciones Anidadas (con N niveles)
def master(valorA, valorB):

    def operacionA():
        print("Operacion A es: ", valorA)

    def operacionB():
        print("Operacion B es: ", valorB)

    
    operacionA()
    operacionB()
    

master(100, "Dany")



