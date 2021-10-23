from random import randint

compNum = randint(0, 100)
count = 0
userNum = 0
while not compNum == userNum:
    userNum = int(input("Input: "))
    if userNum > compNum:
        print(">")
    elif userNum < compNum:
        print("<")
    count += 1
print("Well done, you took", count, "attempts.")
