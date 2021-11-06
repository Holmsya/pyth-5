eatDict = dict.fromkeys([i for i in range(1, 5)])

for i in range(1, 5):
    eatDict[i] = input("Введите название любимого блюда: ")

for item in eatDict.items():
    print(item[0], item[1])

num = int(input("Введите номер блюда, которое хотите исключить: "))
eatDict.pop(num)

for item in eatDict.items():
    print(item[0], item[1])

