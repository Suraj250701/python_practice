# Count number of digits in given number (e.g number=23456 o/p digits=5
number = int(input("Please enter the number : "))
count = 0
while number != 0:
    number = number // 10
    count += 1
print(f"Number of digits in the given number is : {count}")