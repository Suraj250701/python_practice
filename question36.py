# Count no of strings which starts with letter 'M' from list [Use List comprehension]
list_strings = ["Mango", "Apple", "Banana", "Mango", "Melon", "Orange", "Mango"]
print(f"Count of strings starting with 'M' is : {len([i for i in list_strings if i.startswith('M')])}")
