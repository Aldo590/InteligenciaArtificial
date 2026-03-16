# 3.4.7   LAB   La clase Timer

# def two_digits(val):
#     s = str(val)
#     if len(s) == 1:
#         s = '0' + s
#     return s


# class Timer:
#     def __init__(self, hours=0, minutes=0, seconds=0):
#         self.__hours = hours
#         self.__minutes = minutes
#         self.__seconds = seconds

#     def __str__(self):
#         return two_digits(self.__hours) + ":" + \
#                two_digits(self.__minutes) + ":" + \
#                two_digits(self.__seconds)

#     def next_second(self):
#         self.__seconds += 1
#         if self.__seconds > 59:
#             self.__seconds = 0
#             self.__minutes += 1
#             if self.__minutes > 59:
#                 self.__minutes = 0
#                 self.__hours += 1
#                 if self.__hours > 23:
#                     self.__hours = 0

#     def prev_second(self):
#         self.__seconds -= 1
#         if self.__seconds < 0:
#             self.__seconds = 59
#             self.__minutes -= 1
#             if self.__minutes < 0:
#                 self.__minutes = 59
#                 self.__hours -= 1
#                 if self.__hours < 0:
#                     self.__hours = 23


# timer = Timer(23, 59, 59)
# print(timer)
# timer.next_second()
# print(timer)
# timer.prev_second()
# print(timer)

# 3.4.8   LAB   Días de la semana

# class WeekDayError(Exception):
#     pass


# class Weeker:
#     __names = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

#     def __init__(self, day):
#         try:
#             self.__current = Weeker.__names.index(day)
#         except ValueError:
#             raise WeekDayError

#     def __str__(self):
#         return Weeker.__names[self.__current]

#     def add_days(self, n):
#         self.__current = (self.__current + n) % 7

#     def subtract_days(self, n):
#         self.__current = (self.__current - n) % 7


# try:
#     weekday = Weeker('Lun')
#     print(weekday)
#     weekday.add_days(15)
#     print(weekday)
#     weekday.subtract_days(23)
#     print(weekday)
#     weekday = Weeker('Lunes')
# except WeekDayError:
#     print("Lo siento, no puedo atender tu solicitud.")
    
    
# 3.4.10   LAB   Tríangulo

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        per = 0
        for i in range(3):
            per += self.__vertices[i].distance_from_point(self.__vertices[(i + 1) % 3])
        return per


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
    