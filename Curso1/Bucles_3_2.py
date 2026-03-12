# secret_number = 777

# print(
# """
# +================================+
# | ¡Bienvenido a mi juego, muggle!|
# | Introduce un número entero     |
# | y adivina qué número he        |
# | elegido para ti.               |
# |¿Cuál es el número secreto?     |
# +================================+
# """)
# number = 0

# while number != secret_number:
#     number = int(input("Introduce un número: "))
#     if number != secret_number:
#         print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
#     elif number == secret_number:
#         print("¡Bien hecho, muggle! Eres libre ahora.")

# import time


# for i in range(1, 6):
#     print(i, "Missisippi")
# print("Lista o no, aquí vengo!")

#3.2.9   LAB   La sentencia break - atrapado en un bucle

# frasesecreta = "chupacabra"

# frase = ""

# while True:
#     frase = input("¿Cuál es la frase secreta? ")
#     if frase == frasesecreta:
#         print("Has dejado el bucle con éxito.")
#         break

#3.2.10   LAB   La sentencia continue – el Feo Devorador de Vocales

# user_word = input("Ingresa una palabra: ")
# user_word = user_word.upper()

# for letter in user_word:
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#     else:
#         print(letter)

#3.2.11   LAB   La sentencia continue – el Lindo Devorador de Vocales

# user_word = input("Ingresa una palabra: ")
# user_word = user_word.upper()

# for letter in user_word:
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#     else:
#         print(letter)

#3.2.14   LAB   Fundamentos del bucle while


# blocks = int(input("Ingresa el número de bloques: "))

# height = 0
# layer = 1

# while blocks >= layer:
#     blocks = blocks - layer
#     height += 1
#     layer += 1

# print("La altura de la pirámide es:", height)

#3.2.15   LAB   La hipótesis de Collatz


# c0 = int(input("Ingresa un número natural: "))

# steps = 0

# while c0 != 1:
#     if c0 % 2 == 0:
#         c0 = c0 // 2
#     else:
#         c0 = 3 * c0 + 1
    
#     print(c0)
#     steps += 1

# print("Pasos =", steps)