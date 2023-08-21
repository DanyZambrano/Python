# No tienen Indices
# Almacenan Diferente tipos de datos (TIPOS, LISTAS, TUPLAS, DICCIONARIOS)
# Cada valor tiene una llave Unica.  Key: Value


miDiccionario = {}
miDiccionario = dict()

# Key: Value
miDiccionario = {"auto": "Renault"}
miDiccionario = {"autos": 3}
miDiccionario = {3: "Renault"}
miDiccionario = {3: "Renault", "pais": "miPais", "miLista": [1,2,3]}




# Tipo JSON
miDiccionario = {
        "nombre": "Dany",
        "skills": {
            "programacion": True,
            "liderazgo": True
        },
        "metas": ["aws", "apple", "gcp"]
}





# Modificar Dictionario
miDiccionario["nombre"] = "Dany2"
print(miDiccionario)

# Agregar Dictionario
miDiccionario["signo"] = "sagitario"
print(miDiccionario)





# longitud Dictionario
print(len(miDiccionario))







# Obtener un valor
print(miDiccionario["nombre"])
#print(miDiccionario["Nombre"])


# Obtener las keys
print(miDiccionario.keys())


# Obtener los values
print(miDiccionario.values())


# Obtener ambos 
for key, value in miDiccionario.items():
    print(key, value)




# Validar llave (IN)
existe = "Apellido" in miDiccionario
print("Existe?: ", existe)


# Validar llave (GET)
valor = miDiccionario.get("Apellido")
print("El valor es: ", valor)


# Validar llave (GET con segundo argumento)
data = miDiccionario.get("Apellido", "No existe")
print("Data: ", data)


data = miDiccionario.get("Apellido", False)
print("Data: ", data)


data = miDiccionario.get("Apellido", [])
if data:
    print("Existe")





# Valor por defecto
data = miDiccionario.setdefault("Apellido", "Zambrano")
print("Data: ", data)
print("miDiccionario: ", miDiccionario)





# Borrar un elemento Dictionario
del miDiccionario["metas"]
print(miDiccionario)


miDiccionario.pop("skills")
print(miDiccionario)


# Borrar un Dictionario
miDiccionario = {}
print(miDiccionario)

miDiccionario.clear()
print(miDiccionario)

