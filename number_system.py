# num = 255

# # print(f"Decimal: {num}")
# # print(f"Binary: {bin(num)}")
# # print ("Hexadecimal:", hex(num))

# #Binary to Decimal
# binary = "00011"
# print(f"Binary {binary} to Decimal:", int(binary, 2))

# # print("Hexadecimal 0xFF to Decimal:", int("0xFF", 16))


a = "101010"

b = "110011"

# Binary addition
result = bin(int(a, 2) + int(b, 2))[2:]  # Convert to binary and remove '0b' prefix
print(f"Binary addition of {a} and {b} is: {result}")

# Binary subtraction
result = bin(int(a, 2) - int(b, 2))[2:] # Convert to binary and remove '0b' prefix
print(f"Binary subtraction of {a} and {b} is: {result}")
