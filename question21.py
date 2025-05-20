for i in range(1,row_input+1):
    for j in range(i):
        print(count, end = " ")
        if count == 0:
            count = 1
        else:
            count = 0
    count = 1
    print()