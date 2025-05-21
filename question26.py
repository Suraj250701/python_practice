int_row = int(input("Enter the number of rows : "))
for i in range(int_row + 1):
    print(" " * (int_row - i) + '* ' * i)
for i in range(int_row, 0, -1):
    print(' ' * (int_row - i + 1) + '* ' * (i - 1))