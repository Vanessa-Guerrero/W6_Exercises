# Defining variables

names = ['John Doe', 'Lorde ', 'Billie Eilish', 'Megan Thee Stallion']

for name in names:
    first_space_index = name.find(" ") # Creating variable to find the space for first name
    last_space_index = name.rfind(" ") # Creating variable to find the space for last name

    # Extracting the first and last names using the index for spaces
    first_name = name[:first_space_index]  # Everything before the space
    middle_name = name[first_space_index:last_space_index] # Everything between the spaces
    last_name = name[last_space_index + 1:] # Everything after the space (not including the space)

    # Displaying results using splitting method to extract first and last name using index #'s

    print(f'''
Full Name: {name}
First Name: {first_name} 
Middle Name: {middle_name}         
Last Name: {last_name}
''')
