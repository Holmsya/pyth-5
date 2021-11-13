import random

def push(stack, value):
    stack.append(value)

def pop(stack):
    try:
        return stack.pop()
    except IndexError:
        print("stack is empty")

def lastItem(stack):
    print(stack[len(stack) - 1])

def lenStack(stack):
    return len(stack)

stack = []
print(stack)

for i in range(10):
    push(stack, random.randint(0, 1000))
print(stack)

print(pop(stack))

print(stack)
