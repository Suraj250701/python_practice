num_row = int(input("Enter the number of rows : "))
count = 1
for i in range(1, num_row + 1):
    for j in range(i):
        print(f"{count}", end=" ")
        count += 1
    count -= 1
    print()

