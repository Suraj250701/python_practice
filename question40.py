usr_input = input("Enter the character to check if it is vowel or not : ")
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
if usr_input in vowels:
    print(f"{usr_input} is a vowel.")
else:
    print(f"{usr_input} is not a vowel.")