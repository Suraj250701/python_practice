# Find frequency of letter from given string

usr_input_str = input("Please enter a string: ")
search_str = input("Please enter a letter to get its frequency : ")
count = 0
for i in usr_input_str:
    if search_str == i :
        count += 1
print(f"Frequency of letter {search_str} in the given string is : {count}")