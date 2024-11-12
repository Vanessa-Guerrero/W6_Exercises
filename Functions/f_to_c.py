def conv_f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius)

# Fahrenheit values to convert
fahrenheit_values = [212, 90, 72, 32, 0, -40]

# Using for loop to print the converted F temps
for i in fahrenheit_values:
    current_temp_F = i
    current_temp_C = conv_f_to_c(i)
    print(f"{current_temp_F}°F is {current_temp_C}°C")