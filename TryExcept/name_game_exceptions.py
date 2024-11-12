# name = input("Enter a name: ")

def trunc_name(name):
    name = name.lower()

    # Using while loop in a try-except exception handling
    first_letter = None
    while first_letter == None:      # Checking if index isnt 0(first), it'll raise an error
        try:
            first_letter = name[0]
        except IndexError:
            print(f"Error: '{name}' is not a valid name.")
            name = None

    second_letter = None
    while second_letter == None:       # Same as above, but checking for second letter [1]
        try:
            second_letter = name[1]
        except IndexError:
            print(f"Error: '{name}' is not a valid name.")
            name = None

    first_letter = name[0]  
    second_letter = name[1] 
    
    # If the name starts with a vowel
    if first_letter in 'aeiou':  
        return name      # Return full name
    
    # If the name starts with one consonant and then a vowel
    elif second_letter in 'aeiou':  
        return name[1:]  # Truncate the first letter
    
    # If the name starts with two consonants
    else:  
        return name[2:]  # Truncate the first two letters

# Testing the trunc_name function
# print(trunc_name(name))  


# Using generator function for name_game song
def name_game(name):
    truncated_name = trunc_name(name)
    yield f"Name Game for {name.title()}:"
    yield f"{name.title()}, {name.title()}, bo-b{truncated_name}"
    yield f"banana fana fo-f{truncated_name}"
    yield f"me my mo-m{truncated_name}"
    yield f"{name.title()}!"

# Using exception handling for the name
name = None

while name == None:
    try:     
        # Checking if name was a number to raise an error   
        name_input = input('Enter a Name: ').strip()
        int(name_input)
        print("Error: Name cannot be a number.")
        name = None
        print("Let's try again with a different input...\n")
        # Then, checking if input is less than 2
    except ValueError:
        if len(name_input) < 2:
            print("Error: The name must be at least 2 characters long.")
            name = None
            print("Let's try again with a different input...\n")
            # If all is well, name will be used in name game
        else:
            name = name_input
            print(f"Your name, {name}, is valid! Let's play the name game!\n")


# Loop through each name in the list and print the name game song
for x in name_game(name):
        print(x)
