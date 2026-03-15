# 2.5.6   LAB   Mejorando el Cifrado César

# # Ingresa el texto a encriptar.
# text = input("Ingresa un mensaje: ")

# # Ingresar un valor de cambio válido (repitelo hasta que tengas éxito).
# shift = 0

# while shift == 0:
#     try:    
#         shift = int(input("Ingresa el valor de cambio del cifrado (1..25): "))
#         if shift not in range(1,26):
#         	raise ValueError
#     except ValueError:
#         shift = 0
#     if shift == 0:
#         print("¡Valor de cambio inválido!")

# cipher = ''

# for char in text:
#     # ¿Es un letra?
#     if char.isalpha():
#         # Cambia su código.
#         code = ord(char) + shift
#         # Encontrar el código de la primera letra (mayúscula o minúscula).
#         if char.isupper():
#             first = ord('A')
#         else:
#             first = ord('a')
#         # Realizar corrección.
#         code -= first
#         code %= 26
#         # Agregar carácter codificado al mensaje.
#         cipher += chr(first + code)
#     else:
#         # Agregar carácter original al mensaje.
#         cipher += char

# print(cipher)


# 2.5.7   LAB   Palíndromos

# text = input("Ingresa un texto: ")

# # Quitar todos los espacios...
# text = text.replace(' ','')

# # ... y revisar si la palabra es igual en ambos sentidos
# if len(text) > 1 and text.upper() == text[::-1].upper():
# 	print("Es un palíndromo")
# else:
# 	print("No es un palíndromo")
	
 
#  2.5.8   LAB   Anagrams
 
#  str_1 = input("Ingresa la primera cadena: ")
# str_2 = input("Ingresa la segunda cadena: ")

# strx_1 = ''.join(sorted(list(str_1.upper().replace(' ',''))))
# strx_2 = ''.join(sorted(list(str_2.upper().replace(' ',''))))
# if len(strx_1) > 0 and strx_1 == strx_2:
# 	print("Anagramas")
# else:
# 	print("No son anagramas")

# 2.5.10   LAB   ¡Encuentra una palabra!

# word = input("Ingresa la palabra que deseas encontrar: ").upper()
# strn = input("Ingresa la cadena en donde deseas buscar: ").upper()

# found = True
# start = 0

# for ch in word:
# 	pos = strn.find(ch, start) 
# 	if pos < 0:
# 		found = False
# 		break
# 	start = pos + 1
# if found:
# 	print("Si")
# else:
# 	print("No")
	   
    
# 2.5.11   LAB   Sudoku

# Una función que verifica si una lista pasada como argumento contiene
# nueve dígitos del '1' al '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# Una lista de filas que representan el Sudoku.
rows = [ ]
for r in range(9):
    ok = False
    while not ok:
        row = input("Ingresa fila #" + str(r + 1) + ": ")
        ok = len(row) == 9 or row.isdigit()
        if not ok:
            print("Datos de fila incorrectos: se requieren 9 dígitos")
    rows.append(row)

ok = True

# Comprobar si todas las filas son correctas.
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

# Comprobar si todas las columnas son correctas.	
if ok:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break

# Comprobar si todos los subcuadrados (3x3) son correctos.
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = ''
            # Hacer una cadena que contenga todos los dígitos de un subcuadrado.
            for i in range(3):
                sqr += rows[r+i][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break

# Imprimir el veredicto final.
if ok:
    print("Si")
else:
    print("No")