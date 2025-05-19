flag = True
while flag:
    usr_input = input("Enter 0 to exit the program : ")
    if usr_input == "0":
        print("Exiting the program")
        flag = False
    else:
        print("You entered : ", usr_input)