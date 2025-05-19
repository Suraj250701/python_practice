amount_list = int(input("Enter the amount you want to enter in list : "))
my_list = ['A',True,234,45.76]

for i in range(len(my_list)):
    print(f"{my_list[i]} - {type(my_list[i])}")