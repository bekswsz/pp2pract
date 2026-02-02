#1
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

#2
for i in ["hi", " ", "hello", " "]:
    if i == " ":
        continue
    print(i)

#3
for i in range(7):
    if i < 5:
        continue
    print(i)

#4
nums = [-4, -2, -1, 0]
for n in nums:
    if n < 0:
        continue
    print(n)

#5
for word in ["hello", "man", "dog", "freedom"]:
    if len(word) < 4:
        continue
    print(word)