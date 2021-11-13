def printDict(dictionary): # функция для вывода словаря в столбик
    for item in dictionary.items():
        print(item[0], item[1])

eatDict = dict.fromkeys([i for i in range(1, 5)])

for i in range(1, 5):
    eatDict[i] = input("Введите название любимого блюда: ")

printDict(eatDict)

num = int(input("Введите номер блюда, которое хотите исключить: "))
eatDict.pop(num)

printDict(eatDict)

