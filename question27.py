start_num = int(input("Enter the number from which number should start : "))
diff_num = int(input("Enter the Difference between "))
prt_num = int(input("Enter how many number you want to search : "))

for i in range(1, prt_num + 1):
    print(start_num + ((i - 1) * diff_num), end = " ")