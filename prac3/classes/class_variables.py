#1
class MyClass:
    x = 100

a = MyClass()
b = MyClass()
print(a.x, b.x)

#2
class Counter:
    count = 0

Counter.count += 1
print(Counter.count)

#3
class Person:
    species = "Human"

    def __init__(self, name):
        self.name = name

p = Person("Beksultan")
print(p.name, p.species)

#4
class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r

    def area(self):
        return Circle.pi * self.r * self.r

c = Circle(5)
print(c.area())

#5
class Group:
    members = []

Group.members.append("Aidos")
Group.members.append("Beksultan")
print(Group.members)