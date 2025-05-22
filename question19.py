# Write a program to display numbers which are divisible by 13 from given range.

start_num = int(input("Please enter start range to check if it is divisible by 13 : "))
end_num = int(input("Please enter the ending range : "))
if end_num < 13:
    print("Please enter number which is greater than 13.")
else:
    for i in range(start_num, end_num + 1):
        if i % 13 == 0:
            print(f"{i} is divisible by 13.")