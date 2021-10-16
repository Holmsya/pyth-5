var1 = int(input("Input1: "))
var2 = int(input("Input2: "))

if var1 > var2:
    var2 = var2 + 2
    if var1 > var2:
        print("False")
    else:
        print("True")
else:
    print("True")