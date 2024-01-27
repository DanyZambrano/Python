
# Suma de Flotantes
valorA = 0.1
valorB = 0.2
print(valorA + valorB)




# Valores redondeados
resultado = round(2.3)
print(resultado)

resultado = round(2.7)
print(resultado)

resultado = round(4.65)
print(resultado)

resultado = round(4.3, 4)
print(resultado)







# Valor Absoluto
resultado = abs(-5.0)
print(resultado)




# Valor al cuadrado
resultado = pow(4, 2)
print(resultado)








# Validacion de Enteros
valorC = 3.5
resultado = valorC.is_integer()
print(resultado)







# Formateo de valores
valorD = 8.165
print(f"El valor es: {valorD}")

valorD = 1
print(f"El valor es: {valorD:.2f}")
print(f"El valor es: {valorD:.3f}")

valorD = 123456789
print(f"El valor es: {valorD:,}")

valorD = 1234.56
print(f"El valor es: {valorD:,.2f}")

valorE = 0.8
print(f"El valor es: {valorE:.1%}")

valorE = 0.8
print(f"El valor es: {valorE:.2%}")


# Numeros Complejos (Real + Imaginaria)
valorA = 1 + 3j
print(valorA.real)
print(valorA.imag)
print(valorA.conjugate())


valorB = 1 + 2j
valorC = 3 - 4j
print(valorB + valorC)
print(valorB - valorC)
print(valorB * valorC)
print(valorB / valorC)