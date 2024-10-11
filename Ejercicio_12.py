#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día
# tiene un descuento del 60%. Escribir un programa que comience leyendo el
# número de barras vendidas que no son del día. Después el programa debe
# mostrar el precio habitual de una barra de pan, el descuento que se le hace
# por no ser fresca y la ganancia final total.
barras = int(input("Número de barras vendidas que no son del día: "))
precio = 3.49 
descuento = 0.6
coste = barras * precio * (1 - descuento)
print("Precio habitual de una barra de pan: " + str(precio) + "€")
print("Descuento sobre una barra no fresca:  " + str(descuento * 100) + "%")
print("Ganancia final total: " + str(round(coste, 2)) + "€")