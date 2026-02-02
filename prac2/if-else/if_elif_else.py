#1
a = 55
b = 55
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#2
a = 2
b = 121
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#3
temperature = 15

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

#4
ball = int(input("Enter your score: "))

if ball == 140:
    print("Grade: A")
elif ball >= 110:
    print("Grade: B")
elif ball >= 80:
    print("Grade: C")
elif ball >= 50:
    print("Grade: D")
else:
    print("Grade: F")