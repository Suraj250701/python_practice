principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time (in years): "))
rate = float(input("Enter the rate of interest: "))

simple_interest = (principal * time * rate) / 100

print(f"Simple Interest of principal amount {principal} having time duration {time} at the rate of {rate} is : {simple_interest}")