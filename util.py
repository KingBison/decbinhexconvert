

def decimalConvert(decimal):
    decimal = int(decimal)
    print("Decimal: " + str(decimal))
    print("Binary: " + str(bin(decimal)[2:]))
    print("Hex: " + str(hex(decimal)[2:]))

def binaryConvert(binary):
    binary = int(binary)
    print("Binary: " + str(binary))
    print("Decimal: " + str(int(str(binary), 2)))
    print("Hex: " + str(hex(int(str(binary),2))[2:]))

def hexConvert(hex):
    print("Hex: " + str(hex))
    print("Decimal: " + str((int(hex, 16))))
    print("Binary: " + str(bin(int(hex, 16)).zfill(8)[2:]))