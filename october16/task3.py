cycles = int(input("Input: "))

i = 0 # i - итератор

while True:
    print(i < cycles)
    i += 1
    if i == 9002:
        break
print(i < cycles)
