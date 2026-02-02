#1
a = 9
b = 0
if a > b: print("a is greater than b")

#2
a = 67
b = 6767
print("A") if a > b else print("B")

#3
a = 11
b = 22
bigger = a if a > b else b
print("Bigger is", bigger)

#4
a = 6767
b = 6767
print("A") if a > b else print("=") if a == b else print("B")

#5
x = 9
y = 99
max_value = x if x > y else y
print("Maximum value:", max_value)