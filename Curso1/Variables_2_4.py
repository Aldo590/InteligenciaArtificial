#2.4.7 LAB Variables
#Crear variables para almacenar el número de manzanas que tienen John, María y Adán.
#Luego, calcular el número total de manzanas que tienen entre los tres e imprimir el resultado.

John = 3
Maria = 5
Adan = 6
manzanas_total = John + Maria + Adan

print(John, Maria, Adan,sep=", ")

print("El número total de manzanas es:", manzanas_total)


#2.4.9   LAB   Variables: un convertidor simple
#Crear un programa que convierta millas a kilómetros y kilómetros a millas.

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")


#2.4.10   LAB   Operadores y expresiones
#Crear un programa que evalúe la siguiente expresión y muestre el resultado: 3x^3 - 2x^2 + 3x - 1

x =  0
x = float(x)
y = 3*x**3-2*x**2+3*x-1
y = float(y)
print("y =", y)
