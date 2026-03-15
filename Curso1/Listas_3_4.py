# hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.
# print(hat_list)
# hat_list[2] = int(input("Ingrese un número entero: "))

# print(hat_list)
# # Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
# del hat_list[-1]

# # Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
# len(hat_list)
# print(hat_list)

#3.4.11   LAB   Los fundamentos de las listas: los Beatles


beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

for i in range(2):
    beatles.append(input("Ingrese el nombre de un nuevo miembro de los Beatles: "))
    
del beatles[-1]
del beatles[-1]

print(beatles)
    