count = 0
while True:
    name = input("Введите имя того, кого хотите пригласить, иначе введите \"Нет\": ")
    if name.lower() == "Нет".lower():
        break
    else:
        print(name.capitalize(), "был приглашён.")
        count += 1
print("Было приглашено", count, "человек.")

