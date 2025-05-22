# Print half of String in Uppercase

input_string = input("Please enter a string: ")
half_length = len(input_string) // 2
if len(input_string) % 2 == 0:
    half_string = input_string[:half_length].upper() + input_string[half_length:]
else:
    half_string = input_string[:half_length + 1].upper() + input_string[half_length + 1:]
print(f"Half of the string in uppercase is: {half_string}")
