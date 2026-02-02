#1
i = 67
while True:
    if i == 100:
        break
    print(i)
    i += 1

#2
while True:
    password = input("Enter your password: ")
    if password == "2312":
        break

#3
i = 9
while True:
    if i % 2 == 0:
        print("First even:", i)
        break
    i += 1

#4
s = 0
i = 1
while True:
    s += i
    if s >= 100:
        break
    i += 1
print("Sum =", s) #105

#5
while True:
    n = int(input("Enter number: "))
    if n < 0:
        print("n is negative")
        break