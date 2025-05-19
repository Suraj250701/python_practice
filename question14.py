# Print list of items iteratively

amount_list = int(input("Enter the amount you want to enter in list : "))
my_list = []
for i in range(amount_list):
    element = input(f"Enter element {i+1}: ")
    my_list.append(element)

for i in range(len(my_list)):
    print(f"{my_list[i]}")