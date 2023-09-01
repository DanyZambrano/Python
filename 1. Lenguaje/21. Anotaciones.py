# Anotaciones 
# Es una ayuda para el programador / no para el IDE
# Se emplean en variable, constantes, Funciones, Clases, Metodos
# Es una Buena Practica


# Tipo de Datos

# Implicito
valorA  = 7
valorB  = 7.0
valorC  = True
valorD  = "Dany"
valorE  = None


# Explicito
valorA : int   = 7
valorB : float = 7.0
valorC : bool  = True
valorD : str   = "Dany"
valorE : None  = None



# (Sin valor inicial)
valorA : int
valorB : float
valorC : bool
valorD : str
valorE : None

valorA = 7
valorB = 7.0
valorC = True
valorD = "Dany"
valorE = None




# Que pasa si me equivoco en la asignacion?

valorA : int
valorB : float
valorC : bool
valorD : str
valorE : None

valorA = 7.0
valorB = 7
valorC = "True"
valorD = False
valorE = "None"


print(valorA, valorB, valorC, valorD, valorE)



# Listas, Tuplas, Diccioanrios

miLista = [7, 3.1515, True, "Mensaje"]

miTupla = ("Mensaje 23", 7, 3.1415, True, [34, 54, 67], (8 , "mensaje tupla", False))

miDiccionario = {
        "nombre": "Dany",
        "skills": {
            "programacion": True,
            "liderazgo": True
        },
        "metas": ["aws", "apple", "gcp"]
}



miLista : list  = [7, 3.1515, True, "Mensaje"]

miTupla : tuple = ("Mensaje 23", 7, 3.1415, True, [34, 54, 67], (8 , "mensaje tupla", False))

miDiccionario : dict = {
        "nombre": "Dany",
        "skills": {
            "programacion": True,
            "liderazgo": True
        },
        "metas": ["aws", "apple", "gcp"]
}




# Funciones
def suma(valorA: int, valorB: int) -> int:
    return valorA + valorB

print(suma(2, 3))














# Clases
class clasePadre:

    def __init__(self, altura : float, peso : int):
        self.altura = altura
        self.peso = peso
    
    def estudiar():
        print("Estudiar")










