row_input = int(input("Please enter the number of rows : "))

for i in range(1,row_input+1):
    for j in range(i):
        print(i, end = " ")
    print()