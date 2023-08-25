

# Funciones Lamdas (funciones anonimas)
# Tareas pequeñas y muy puntuales
# no tienen nombres de funcion
# lambda <parametros> : <funcion>

temperatura = lambda medicion: medicion * 10
print(temperatura(2.3))








# Funciones con Callback
# son usadas como argumentos para otras funciones

def funcionA(n):
    return n[0]*n[1]

def funcionB(func, n):
    return func(n)


notas = (8, 5)
resultado = funcionB(funcionA, notas)

print("resultado =", resultado)


