with open("pi_million_digits.txt", "r") as pi:
    # print(pi.readline())
    pi_lines = pi.readlines()
    print(pi_lines)

    user_birthday = input("Enter your birthday in the format MMDDYY: ")
    birthday_found = None

    for i in pi_lines:
        if user_birthday in i:
            print("Your birthday is in the first million digits of pi!")
            birthday_found = 1  # Set the tracker to indicate the birthday was found
            break  # Exit the loop since the birthday has been found
    
    pi_string = ''
    for line in pi_lines:
        pi_string += line.strip()

    if birthday_found != 1:
        print("Sorry, your birthday was not found in the first million digits of pi.")
    else:
        birthday_pos = pi_string.index(user_birthday) -1

    # print(pi_lines[0]/n)
    # print(pi_lines[1]/n)
    # print(len(pi_lines[0]))
    # print(len(pi_lines[1]))
