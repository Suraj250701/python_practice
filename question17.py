# Write a program to display number names of entered number e.g number="345" output = Three Four Five
num = int(input("Please enter the number : "))
num_word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
num_str = str(num)
for i in range(len(str(num))):
    if i == len(num_str) - 1:
        print(num_word[int(str(num)[i])], end = " ")
    else:
        print(num_word[int(str(num)[i])], end = " ")
    