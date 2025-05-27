# Write a program to find GCD (Greatest Common Divisor) of 2. 
user_input = input("Enter two numbers to find GCD : ")

num1, num2 = [int(x) for x in user_input.split()]
while num2:
    num1, num2 = num2, num1 % num2
print(f"GCD of the given numbers is {num1}.")
