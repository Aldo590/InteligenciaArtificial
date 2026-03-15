# texto = "hola mundo"
# lista = ["uno", "dos", "tres"]

# print("capitalize:", texto.capitalize())

# print("center:", texto.center(20, "-"))

# print("endswith:", texto.endswith("mundo"))

# print("find:", texto.find("m"))

# print("isalnum:", "abc123".isalnum())

# print("isalpha:", "abc".isalpha())

# print("isdigit:", "123".isdigit())

# print("islower:", texto.islower())

# print("isspace:", "   ".isspace())

# print("isupper:", "HOLA".isupper())

# print("join:", "-".join(lista))

# print("lower:", "HOLA".lower())

# print("lstrip:", "   hola".lstrip())

# print("replace:", texto.replace("hola", "adios"))

# print("rfind:", texto.rfind("o"))

# print("rstrip:", "hola   ".rstrip())

# print("split:", texto.split())

# print("startswith:", texto.startswith("hola"))

# print("strip:", "   hola   ".strip())

# print("swapcase:", "HoLa".swapcase())

# print("title:", texto.title())

# print("upper:", texto.upper())

#2.3.25   LAB   Tu propio separador

# def mysplit(strng):
#     if not strng or strng.isspace():
#         return []
    
#     lista = []
#     palabra = ""
#     en_palabra = False
    
#     for char in strng:
#         if char != " ":
#             palabra += char
#             en_palabra = True
#         elif en_palabra:
#             lista.append(palabra)
#             palabra = ""
#             en_palabra = False
            
#     if en_palabra:
#         lista.append(palabra)
        
#     return lista