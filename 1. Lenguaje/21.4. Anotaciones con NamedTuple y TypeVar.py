

# NamedTuple
# Clases inmutables
# No pueden modificarse en tiempo de ejecucion
from typing import NamedTuple

class Pagina(NamedTuple):
    nombre: str
    url: str
  
# Creando a NamedTuple
sitio1 = Pagina('Google',
                   'www.google.com')

sitio2 = Pagina('Apple',
                   'www.apple.com')
  
print(sitio1)
print(sitio2)






# TypeVar
# Es un objeto generico, por lo tanto complejo
from typing import TypeVar

T = TypeVar("T")

def identidad(arg: T) -> T:
    return arg