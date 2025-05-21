fibo_ser = int(input("Enter the number to get series of fibonacci numbers : "))
first_num = 0
second_num = 1
sum_num = 0
print(f"{first_num} {second_num}", end=" ")
while fibo_ser - 2 > 0 :
    sum_num = first_num + second_num
    print(f"{sum_num}", end = " ")
    first_num = second_num
    second_num = sum_num
    fibo_ser -= 1