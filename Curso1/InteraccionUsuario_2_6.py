#2.6.2 La función input() con un argumento

anything = input("Dime lo que sea...")
print("Hmm...", anything, "...¿en serio?")


#2.6.9   LAB   Entradas y salidas simples
#Elaborar un programa que solicite al usuario 2 valores numéricos,
#y luego imprima la suma, resta, multiplicación y división de ambos números.

varA = float(input("Ingresa un valor numérico para la variable A: "))
varB = float(input("Ingresa un valor numérico para la variable B: "))

# mostrar el resultado de la suma aquí
print("La suma de", varA, "y", varB, "es:", varA + varB)
# mostrar el resultado de la resta aquí
print("La resta de", varA, "y", varB, "es:", varA - varB)
# mostrar el resultado de la multiplicación aquí
print("La multiplicación de", varA, "y", varB, "es:", varA * varB)
# mostrar el resultado de la división aquí
print("La división de", varA, "y", varB, "es:", varA / varB)
print("\n¡Eso es todo, amigos!")

#2.6.10   LAB   Operadores y expresiones
#Programa que evalúe la siguiente expresión

x = float(input("Ingresa el valor para x: "))
y= (1/(x+(1/(x+(1/(x+(1/x)))))))

#2.6.11   LAB   Operadores y expresiones – 2

#La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado,
#expresándolo en horas y minutos. La hora de inicio se da como un par de horas (0..23) y minutos (0..59). 
#El resultado debe ser mostrado en la consola.

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
mins = mins + dura # encuentra el número total de minutos
hour = hour + mins // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
mins = mins % 60 # corrige los minutos para que estén en un rango de (0..59)
hour = hour % 24 # corrige las horas para que estén en un rango de (0..23) 
print(hour, ":", mins, sep='')

print("y =", y)