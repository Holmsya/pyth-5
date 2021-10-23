from random import randint

bottles = randint(1, 20)
print("There are", bottles, "green bottles hanging on the wall, and if 1 green bottles will be hanging on the wall?")
while bottles != 0:
    answer = int(input("How many green bottles will be hanging in the wall? "))
    if answer == bottles - 1:
        print("There will be,", bottles - 1, "green bottles hanging on the wall")
        exit()
    else:
        print("No, try again")
        bottles -= 1
print("There are no more green bottles hanging on the wall.")

