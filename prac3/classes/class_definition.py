#1
class MyClass:
    x = 5

obj = MyClass()
print(obj.x)

#2
class Car:
    brand = "Toyota"
    year = 2024

c = Car()
print(c.brand, c.year)

#3
class Empty:
    pass

e = Empty()
print(type(e))

#4
class Engine:
    power = "100 HP"

class Vehicle:
    engine = Engine()

v = Vehicle()
print(v.engine.power)

#5
class StudentGroup:
    students = ["Beksultan", "Bekzhan", "Aidos"]

sg = StudentGroup()
print(sg.students)