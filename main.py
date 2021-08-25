from util import *

end = False

while not end:
    print("Enter d, b or h for which number type you want information for")
    print("Enter e to exit")
    print("")
    inp = input()
    if inp == "d":
        print("Enter decimal: ")
        num = input()
        decimalConvert(num)
    elif inp == "b":
        print("Enter binary: ")
        num = input()
        binaryConvert(num)
    elif inp == "h":
        print("Enter hex: ")
        num = input()
        hexConvert(num)
    elif inp == "e":
        end = True
    else:
        print("invalid input")
        print("try again")
    print()
    print()

print("program terminated")

