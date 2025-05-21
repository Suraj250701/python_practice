fact_num = int(input("Enter the number to find its factotial : "))
mul = 1
while(fact_num > 0):
    mul = fact_num * mul
    if fact_num > 1 :
        print(f"{fact_num} *",end=" ")
    else :
        print(f"{fact_num}")
    fact_num -= 1
print(f"factorial of given number is {mul}")