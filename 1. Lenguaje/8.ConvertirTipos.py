edad = input("Ingresa tu Edad: ")

edadEntero = int(edad)
print(edadEntero)
print(type(edadEntero))

edadFloat = float(edad)
print(edadFloat)

entrada = input("Usted va asistir al evento (si/no): ")
asistencia = entrada == "si"
print(asistencia)










#Refactorizar el codigo
edadEntero = int(input("Ingresa tu Edad: "))
edadFloat = float(input("Ingresa tu Edad: "))
asistencia = input("Usted va asistir al evento (si/no): ") == "si"
print(edadEntero, edadFloat, asistencia)