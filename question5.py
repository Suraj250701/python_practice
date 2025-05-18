principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time (in years): "))
rate = float(input("Enter the rate of interest: "))

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal
print(f"Compound Interest of principal amount {principal} having time duration {time} at the rate of {rate} is : {compound_interest}")