binary_number = input("Enter a binary number: ")
length = len(binary_number)
binary_number = int(binary_number)
decimal_number = 0

while (length > 0):
    decimal_number = int(decimal_number + binary_number % 10 * (2 ** (length - 1)))
    binary_number = binary_number/10
    length = length - 1

print("Decimal number is: ", decimal_number)