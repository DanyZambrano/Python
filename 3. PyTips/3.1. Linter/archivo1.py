def sumatoria(a, b, c):
    if a > 0 and b > 0:
        suma = a + b + c
        print("suma:", suma)
    else:
        print("a y b deben ser positivos")


class Otra_clase:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y

    def Suma(self):
        return self.x + self.y


clase_Instanciada = sumatoria(3, 5)

resultado = clase_Instanciada.Suma()

print("resultado:", resultado)

sumatoria(1, 2, 3)
