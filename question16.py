first_num = int(input("Please enter 1st number : "))
second_number = int(input("Please enter 2nd number : "))

# apply the logic to check if first_num is 0 or second_number is 0
# and change the value of first_num or second_number accordingly
if first_num == 0:
    first_num = 1
elif second_number == 0:
    second_number -= 1


while first_num <= second_number:
    if first_num % 2 == 0:
        print(f"{first_num}")
    first_num += 1

