#Calculo IMC
# def bmi(weight, height):
#     if height < 1.0 or height > 2.5 or \
#     weight < 20 or weight > 200:
#         return None

#     return weight / height ** 2


# print(bmi(352.5, 1.65))

#Triángulos

# def is_a_triangle(a, b, c):
#     if a + b <= c:
#         return False
#     if b + c <= a:
#         return False
#     if c + a <= b:
#         return False
#     return True


# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 3))

#Evaluando el área de un triángulo

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
 
 
# def heron(a, b, c):
#     p = (a + b + c) / 2
#     return (p * (p - a) * (p - b) * (p - c)) ** 0.5
 
 
# def area_of_triangle(a, b, c):
#     if not is_a_triangle(a, b, c):
#         return None
#     return heron(a, b, c)
 
 
# print(area_of_triangle(1., 1., 2. ** .5))
 
 #Factoriales
 
#  def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
 
#     product = 1
#     for i in range(2, n + 1):
#         product *= i
#     return product
 
 
# for n in range(1, 6): # probando
#     print(n, factorial_function(n))

#Números Fibonacci

# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
 
#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum
 
 
# for n in range(1, 10): # probando
#     print(n, "->", fib(n))
 