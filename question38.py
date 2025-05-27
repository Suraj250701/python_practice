# Write a program to find given item from tuple
tpl_size = int(input("Enter the size of tuple : "))
tpl = tuple(input(f"Enter item {i+1} : ") for i in range(tpl_size))
usr_input = input("Enter the item to search in tuple : ")
if usr_input in tpl:
    print(f"{usr_input} is present in the tuple.")
else:
    print(f"{usr_input} is not present in the tuple.")
    
