#1
for i in range(10):
    if i == 2:
        break
    print(i)

#2
for a in "hello":
    if a == "o":
        break
    print(a)

#3
nums = [-1, 2, 0, -5]
for n in nums:
    if n < 0:
        break
    print(n)

#4
for i in range(7):
    if i % 2 == 0:
        print("First even:", i)
        break

#5
for word in ["go", "run", "stop", "wait"]:
    if word == "stop":
        break
    print(word)