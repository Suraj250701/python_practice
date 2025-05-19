digit = 0
string = 0
usr_str = input("Please enter the string : ")

for i in usr_str:
    if i.isdigit() :
        digit += 1
    else :
        string += 1

print(f"Digits = {digit} and Letters = {string}")