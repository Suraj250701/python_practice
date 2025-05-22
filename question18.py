num = int(input("Enter the number to find the series : "))
fact_num = 1
sum_num = 0
for i in range(1, num + 1):
    fact_num = fact_num * i
    sum_num += (1 / fact_num)
    if i == num:
        print(f"1/{i}! = ", end = " ")
    else:
        print(f"1/{i}! + ", end = " + ")
print(f"Sum of the series is : {sum_num}")