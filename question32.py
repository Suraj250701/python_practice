check_arm = int(input("Enter the number to check if it is armstrong or not : "))
temp_check = check_arm
sum_num = 0
for i in range(len(str(check_arm))):
    temp_num = temp_check % 10
    sum_num += (temp_num ** len(str(check_arm)))
    temp_check = temp_check // 10

if check_arm == sum_num :
    print(f"{check_arm} is an armstrong number.")
else :
    print(f"{check_arm} is not an armstrong number.")