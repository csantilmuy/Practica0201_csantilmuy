# Escribir un programa que lea un entero positivo, , introducido por el usuario
# y después muestre en pantalla la suma de todos los enteros desde 1 hasta .
# La suma de los  primeros enteros positivos puede ser calculada de la
# siguiente forma: suma = (n * (n + 1)) / 2
n = int(input("Escribe un número entero: "))
suma = (n * (n + 1)) / 2
print("La suma de todos los enteros desde 1 hasta " + str(n) + " es " + str(suma))