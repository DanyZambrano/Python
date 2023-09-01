# Alias
# Asignar un nombre mas legible

from typing import Union
sumatoria = Union[None, int]

def sumaCon(valorA: int, valorB: int) -> sumatoria:
    if valorA == 2:
        return None
    else:
        return valorA + valorB







# Literal
# Es un Listado con posibles opciones
# Parecido a un Emuns

from typing import Literal
generos = Literal["F", "M"]

def registro(nombre: str, password: str, genero: generos):
    print("genero: ", genero)

registro("Samanta", "1234", "N")











# Literal
# Es un Listado con posibles opciones
# Parecido a un Emuns

from typing import Literal
generos = Literal["F", "M", "B"]

def registro(nombre: str, password: str, genero: generos):
    print("genero: ", genero)

registro("Samanta", "1234", "N")


