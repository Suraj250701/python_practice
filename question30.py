# Check whether given number is prime or not
chk_prime = int(input("Enter the numbers to check if it is prime or not : "))
if chk_prime < 0:
    print("Please enter a positive number.")
elif chk_prime == 0:
    print("Given number is zero.")
elif chk_prime == 1 or chk_prime == 2 or chk_prime == 3:
    print(f"{chk_prime} is a prime number.")
else: 
    for i in range(2,chk_prime):
        if chk_prime % i == 0:
            print(f"{chk_prime} is a not prime number.")
            break
        else :
            print(f"{chk_prime} is a prime number.")
            break
        