# Print even numbers from give range without using % .

start_num = int(input("Enter the first number : "))
last_num = int(input("Enter the last number : "))

if start_num == 0:
    start_num = 1
elif last_num == 0:
    last_num -= 1

for i in range(start_num, last_num + 1):
    if i == 0:
        continue
    if i & 1 == 0:
        print(f"{i} is even")