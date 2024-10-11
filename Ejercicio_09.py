#Escribir un programa que pregunte al usuario una cantidad a invertir, el
# interés anual y el número de años, y muestre por pantalla el capital
# obtenido en la inversión.
cantidad_a_invertir = float(input("¿Cantidad a invertir?: "))
interes_anual = float(input("¿Interés anual?: "))
años = int(input("¿Cuántos años?: "))
print("Capital obtenido: " + str(round(cantidad_a_invertir * (interes_anual / 100 + 1) ** años, 2)))