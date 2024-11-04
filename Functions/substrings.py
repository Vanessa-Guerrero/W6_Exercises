# PART 1 and 2

# names = ['John Doe', 'Grace Flores', 'JB Oinonen']

# for name in names:

#     space_index = name.find(" ")  # Finding the space index
#     first_name = name[:space_index] #  First name is up to the space index
#     last_name = name[space_index + 1:] # Last name is 1 + the space index (to not include the space)

#     print(f'''
# Full name: {name}
# First name: {first_name}
# Last name: {last_name}
# ''')


names = ['Lorde', 'Billie Eilish', 'Megan Thee Stallion']

for name in names:
    first_space_index = name.find(" ")  # Finding the space from left to right
    last_space_index = name.rfind(" ")  # Finding the space from right to left

    if first_space_index == -1:  # Used if there's only one name with no space (First name only)
        print (f'Full name: {name} \nFirst Name: {name} \n')

    elif first_space_index == last_space_index:   # Used if there's two names (First and last name)
        first_name = name[:first_space_index]     # First name is up to the space index
        last_name = name[first_space_index + 1:]  # Last name is 1 + the space index (to not include the space)
        print (f'Full name: {name} \nFirst Name: {first_name} \nLast Name: {last_name}')

    else:                                          # Used for 3 names (First, middle, or last name)
        first_name = name[:first_space_index]  
        middle_name = name[first_space_index + 1:last_space_index]  # Middle name is found between the first (+1) & last space
        last_name = name[last_space_index + 1:]  
        print (f'''
Full name: {name}
First Name: {first_name}
Middle Name: {middle_name}
Last Name: {last_name}
''')
