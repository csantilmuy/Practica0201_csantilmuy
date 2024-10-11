#Escribir un programa que pregunte al usuario por el número de horas
# trabajadas y el coste por hora. Después debe mostrar por pantalla la paga
# que le corresponde.
horas_trabajadas = float(input("¿Cuantas horas has trabajado?: "))
coste_por_hora = float(input("¿Cuanto cobras por hora?: "))
paga_correspondiente = horas_trabajadas * coste_por_hora
print("Tu paga:", paga_correspondiente)