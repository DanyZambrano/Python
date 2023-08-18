
################################
#   No se pueden modificar
################################

cadena = "Test de Certificacion"
#cadena[0] = "M"


cadena = cadena + "!"
print(cadena)



















###########################
#      Concatenar
###########################
valorA = "Hola como"
valorB = "te va?"
valorC = valorA + " " + valorB
print(valorC)


valorA = "Hola como"
valorB = "te va?"
valorC = 'La oracion es >> %s %s' %(valorA, valorB)
print(valorC)











###########################
#         SPLIT()
###########################

#Split retorna un listado de elementos
valorA = "El mundo es plano!"
valorB = valorA.split()
print("valorA separado es: ", valorB)


valorA = "El.mundo.es.plano!"
valorB = valorA.split(".")
print("valorA separado es: ", valorB)


valorA = 'El "mundo" es plano!'
valorB = valorA.split('"')
print("valorA separado es: ", valorB)


#Split con saltos
valorA = 'El#mundo#es#plano!'
valorB = valorA.split('#', 2)
print("valorA separado es: ", valorB)













###########################
#         JOIN()
###########################

cadena1 = "Como te va?"
oracionCompleta = '-'.join(cadena1)
print(oracionCompleta)
print(type(oracionCompleta))


myTuple = ("John", "Peter", "Vicky")
oracionCompleta = " - ".join(myTuple)
print(oracionCompleta)





###########################
#       COUNT()
###########################
valorC = "Somos developers que en un sentido figurado, programamos algo, Somos creadores!"
coincidencia = valorC.count("o")
print(coincidencia)





###########################
#       lower()
###########################
valorA = 'SOMOS develOpers'
print(valorA.lower())



###########################
#       startswith()
#       endswith()
###########################
valorA = 'SOMOS develOpers'
print(valorA.startswith("SOMOS"))
print(valorA.endswith("develOperx"))





###########################
#       center()
#       rjust()
#       ljust()
###########################

mensaje = "Cerveza"

x = mensaje.rjust(20)
print(x, "es mi bebida bebida.")

x = mensaje.ljust(20)
print(x, "es mi bebida bebida.")

x = mensaje.center(20)
print(x, "es mi bebida bebida.")