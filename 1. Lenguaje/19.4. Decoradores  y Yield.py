

# Funciones con Decoradores
# codigo legible, reducir codigo, evitar duplicados
# <<< Es un Patron de diseno que permite modificar la funcionalidad de una funcion
# envolviendola en otra funcion :) >>>


def logica(func):
    def interna(a, b):
        print("dividire", a, "y", b)
        if b == 0:
            print("no divisible!!!")
            return

        return func(a, b)
    return interna

@logica
def dividir(a, b):
    print(a/b)

dividir(10, 2)





# Funcion Yield
# se implementa yield (suspendemos la ejecucion de la funcion, luego que retorne puede continuar)

def calculo():
    i = 1
    while True:
        yield i*i
        i += 1
    
 
for num in calculo():
    if num > 30:
        break
    print(num)


