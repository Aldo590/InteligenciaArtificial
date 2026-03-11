#n=0
#input(n)
#print("Mayor que 100:", n>100)
#print("Menor o igual que 100:", n<100)

#Frase = input()
#if Frase == "ESPATIFILIO":
#    print("¡Sí! ¡Es un espatifilio!")
#elif Frase == "espatifilio":
#    print("No, ¡quiero un gran Espatifilo!")
#Else: print("Espatifilio!, ¡No", Frase, "!")

fecha = int(input("¿En qué año estamos? "))

if fecha < 1582:
    print("No dentro del calendario gregoriano")
elif fecha % 4 != 0:
    print("Es año común")
elif fecha % 100 != 0:
    print("Es año bisiesto")
elif fecha % 400 != 0:
    print("Es año común")
else:
    print("Es año bisiesto")