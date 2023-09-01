# Anotaciones con typing

# Typing, es un modulo con clases reservadas
from typing import List, Dict, Tuple

miLista : List[int]  = [7, 8, 11, 12]

miTupla : Tuple[str, str, int] = ("Mensaje 23", "Mensaje 24", (1, 6, 78))

miDiccionario : Dict[str,  str] = {
        "nombre": 7
}




# Funciones (parametros y el return)
from typing import List, Dict, Tuple

def suma(valorA: int, valorB: int) -> int:
    return valorA + valorB

print(suma(2, 3))


def sumaMejorada(valores: List[int]) -> int:
    return sum(numeros)

numeros : List[int] = [2,3,5]
print(sumaMejorada(numeros))


