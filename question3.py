first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

# Use nested ternary operators to find the maximum
maximum = first_number if (first_number > second_number and first_number > third_number) else (second_number if second_number > third_number else third_number)

# Display the result
print("The maximum number is:", maximum)