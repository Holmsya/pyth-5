num = 0
while not 10 <= num <= 20:
    num = int(input("Input num from 10 to 20: "))
    if num < 10:
        print("Too low")
    elif num > 20:
        print("Too high")
print("Thank you")
