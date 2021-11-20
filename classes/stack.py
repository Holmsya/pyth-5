import random

class Stack:
    def __init__(self):
        self.__stack = []
        print("Стек создан.")

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        try:
            return self.__stack.pop()
        except IndexError:
            print("Стек пуст.")

    def peak(self):
        try:
            print(self.__stack[len(self.__stack) - 1])
        except IndexError:
            print("Стек пуст.")

    def lenStack(self):
        return len(self.__stack)


someStack = Stack()
for i in range(random.randint(1, 20)):
    someStack.push(random.randint(0, 100))
for i in range(someStack.lenStack() + 1):
    print(someStack.pop(), end=' ')
print()

