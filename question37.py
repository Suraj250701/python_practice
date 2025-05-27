# Count no of string which contains particular letter or not with List and List Comprehension

lst_size = int(input("Please enter the size of list : "))
lst_str = [input(f"Please enter the {i+1} element : ") for i in range(lst_size)]
letter = input("Please enter the letter to check if it is present in the string or not : ")

# Count no of string which contains particular letter or not with List

count = 0
for i in lst_str:
    if letter in i:
        count += 1
print(f"Count of strings containing letter '{letter}' is : {count}")



#with list comprehension

print(f"Count of strings containing letter '{letter}' using List Comprehension is : {len([i for i in lst_str if letter in i])}")   