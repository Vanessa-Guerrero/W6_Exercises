name = input("Enter a name: ")

def trunc_name(name):
    name = name.lower()
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

# Loop through each name in the list and print the name game song
for x in name_game(name):
        print(x)