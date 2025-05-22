# Print list of prime numbers from given range

start_num = int(input("Please enter the starting range : "))   
end_num = int(input("Please enter the ending range : "))
prime_list = []
for i in range(start_num, end_num + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_list.append(i)

print(f"List of prime numbers from {start_num} to {end_num} is : {prime_list}")
