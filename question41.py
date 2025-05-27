usr_input = input("Enter the strings to find number of vowels and consonants : ")
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
vow_count = 0
con_count = 0
for usr_input in usr_input:
    if usr_input in vowels:
        vow_count += 1
    else:   
        con_count += 1
print(f"Vowels - {vow_count} & Consonants - {con_count}")