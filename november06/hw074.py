color = ["white", "red", "blue", "black", "cyan", "violet", "purple", "brown", "grey", "green"]

num1 = int(input("Введите начальное число от 0 до 4: "))
num2 = int(input("Введите конечное число от 5 до 9: "))

# print(color[num1:num2])

for i in range(num1, num2):
    print(color[i])
