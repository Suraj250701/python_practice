# Write a program to display number names of entered number e.g number="345" output = Three Four Five
num = int(input("Please enter the number : "))
num_word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
num_str = str(num)
for i in range(len(str(num))):
    if i == len(num_str) - 1:
        print(num_word[int(str(num)[i])], end = " ")
    else:
        print(num_word[int(str(num)[i])], end = " ")






# num_word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# num_int = int(input("Please enter the number : "))
# while len(str(num_int)) >= 0:
#     if num_int == 0:
#         print(num_word[0])
#         break
#     elif num_int < 0:
#         print("Please enter a positive number")
#         break
#     elif num_int <= 9:
#         last_digit = num_int % 10
#         print(num_word[last_digit])
#         num_int = num_int // 10
    