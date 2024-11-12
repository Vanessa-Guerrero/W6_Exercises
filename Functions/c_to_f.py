def conv_c_to_f(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit)

# Celsius values to convert
celsius_values = [100, 45, 19, 0, -7, -40]

# Using for loop to print the converted F temps
for i in celsius_values:
    fahrenheit = conv_c_to_f(i)
    print(f"{i}°C is {fahrenheit}°F")