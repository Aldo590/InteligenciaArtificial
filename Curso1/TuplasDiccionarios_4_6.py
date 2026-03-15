#Tuplas

# my_tuple = (1, 10, 100, 1000)

# print(my_tuple[0])
# print(my_tuple[-1])
# print(my_tuple[1:])
# print(my_tuple[:-2])

# for elem in my_tuple:
#     print(elem)

#Diccionarios

# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
# phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
# empty_dictionary = {}

# print(dictionary['cat'])
# print(phone_numbers['Suzy'])

# Las tuplas y los diccionarios pueden trabajar juntos

# school_class = {}

# while True:
#     name = input("Ingresa el nombre del estudiante: ")
#     if name == '':
#         break
    
#     score = int(input("Ingresa la calificación del estudiante (0-10): "))
#     if score not in range(0, 11):
# 	    break
    
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
        
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)
