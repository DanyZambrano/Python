

# Optional
# Union or | (depende de la version de python)
# cuando una variable toma diferente tipo de datos
from typing import Union

def sumaCon(valorA: int, valorB: int) -> Union[None, int]:
    if valorA == 2:
        return None
    else:
        return valorA + valorB


# | esto es llamado pipe y es lo mismo que Union
def sumaCon(valorA: int, valorB: int) ->  None | int:
    if valorA == 2:
        return None
    else:
        return valorA + valorB
 






# Any 
# Los usamos cuando no sabemos el tipo o no desees forzar un tipo
# Any es Ambiguo y no permite hacer seguimiento del codigo
from typing import Any

valorA : Any
valorB : Any

valorA = 7
valorB = "Dany"



def suma(valorA: Any, valorB: Any) -> Any:
    return valorA + valorB

print(suma(2, 3.0))
