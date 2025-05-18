mode_temperature = input("Enter the mode of temperature (C for Celsius/F for Fahrenheit): ")

if mode_temperature == "C":
    temperature = float(input("Enter the temperature in Celsius: "))
    temperature = (temperature * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {temperature}")
elif mode_temperature == "F":
    temperature = float(input("Enter the temperature in Fahrenheit: "))
    temperature = 5/9 * (temperature - 32)
    print(f"The temperature in Celsius is: {temperature}")
else:
    print("Invalid mode of temperature. Please enter C for Celsius or F for Fahrenheit.")