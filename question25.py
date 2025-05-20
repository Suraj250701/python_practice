row_input = int(input("Please enter the number of rows : "))

for i in range(row_input,0,-1):
    # for j in range(i):
    for j in range(i):
        print("*", end = " ")
    print()



# Another way to print the same pattern

# for i in range(row_input, 0, -1):
#     print('*' * i)