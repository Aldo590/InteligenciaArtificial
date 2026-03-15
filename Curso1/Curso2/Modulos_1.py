print("Repaso rápido del Módulo 1")
print()

print("Un módulo es un archivo de Python que contiene funciones o variables.")
print("Para usar un módulo se utiliza la palabra: import")
print()

# Pregunta 1
respuesta = input("Pregunta 1: ¿Qué palabra se usa para cargar un módulo?\n")

if respuesta == "import":
    print("Correcto")
else:
    print("Incorrecto. La respuesta es: import")

print()

print("Python tiene muchos módulos como math, random y platform.")
print()

# Pregunta 2
respuesta = input("Pregunta 2: ¿Cómo se llama la variable que guarda el nombre del módulo actual?\n")

if respuesta == "__name__":
    print("Correcto")
else:
    print("Incorrecto. La respuesta es: __name__")

print()
print("Fin del repaso")