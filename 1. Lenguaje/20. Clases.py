# Las clases no pueden estar vacias
# puedes crear N cantidad de clases

# Crear / Definir una Clase
class NombreClase:
    pass



# Instanciar la clase
myClase = NombreClase()
print(myClase)



# Atributos de una clase
class Login:
    email = "danyzambranososa@gmail.com"
    password = "12345"

print(Login)
print(Login.email)
print(Login.password)


Login.password = "54321"
print(Login)
print(Login.email)
print(Login.password)


# Que pasa si el atributo no existe?
#print(Login.forgotPassword)







# Metodos
# self hace referencia al objeto clase
class Auto:

    def __init__(self, color, marca):
        self.color = color
        self.marca = marca


auto1 = Auto("negro", "toyota")
auto2 = Auto("amarillo", "bmw")

print(auto1.__dict__)
print(auto2.__dict__)







# Herencia
class clasePadre:
    pass

class claseHijo(clasePadre):
    pass




class clasePadre:
    
    def estudiar():
        print("Estudiar")

    def crear():
        print("Crear proyectos")


class claseHijo(clasePadre):
    pass



herencia = claseHijo()
print("La herencia es: ", herencia)

herencia.estudiar
herencia.crear










# Se permite la herencia multiple
class clasePadre:

    def __init__(self, altura, peso):
        self.altura = altura
        self.peso = peso
    
    def estudiar():
        print("Estudiar")

    def crear():
        print("Crear proyectos")


class claseMadre:

    def velocidad():
        print("Estudiar")

    def analisis():
        print("Crear proyectos")

    def creatividad():
        print("Crear proyectos")
        


class claseHijo(clasePadre, claseMadre):
    pass


herencia = claseHijo("1.80", "azul")
print(herencia.__dict__)


# Sobrecarga de Metodos
# una clase hija modifica metodos de la clase padre
# A la acción de poder modificar el comportamiento de una método de la clase padre, para que así se adecue a las necesidades de la clase hija.
# se busca de izquierda a derecha
class clasePadre:
    
    def estudiar():
        print("Estudiar")

    def crear():
        print("Crear proyectos")


class claseMadre:
    
    def velocidad():
        print("Estudiar")

    def analisis():
        print("de la visa")

    def creatividad():
        print("Crear vida")
        


class claseHijo(clasePadre, claseMadre):

    def crear(self):
        print("Crear tareas")

    def creatividad(self):
        print("jugar")


herencia = claseHijo()
herencia.analisis
herencia.creatividad
herencia.crear





# Super
# usada para feferirse a la superclase
# accede a la clase inmediata

class clasePadre:

    def estudiar():
        print("Estudiar")

    def crear():
        print("Crear proyectos")


class claseMadre:

    def __init__(self, altura, peso):
        self.altura = altura
        self.peso = peso
    
    def velocidad():
        print("Estudiar")

    def analisis():
        print("de la visaCVCVVVC")

    def creatividad():
        print("Crear vida")
        


class claseHijo(clasePadre, claseMadre):

    def crear(self):
        super().claseMadre("1.90", "78kg")
        print("Crear tareas")

    def creatividad(self):
        print("jugar")


herencia = claseHijo("1.50","90kg")






# Metodo de Clase
# significa que no creo una instancia,, sino que empleo directamente el metodo de la clase
# CLS es por convencion en python
class Calculo:
    valorA = 2

    @classmethod
    def suma(cls, valorB):
        return cls.valorA + valorB

respuesta = Calculo.suma(5)
print(respuesta)
