my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

lista_unica = []

for num in my_list:
    if num not in lista_unica:
        lista_unica.append(num)

my_list = lista_unica

print("La lista con elementos únicos:")
print(my_list)