with open("about_me.txt", "r") as f:
    # print(f.read())  # This will print the entire contents of the file
    # print(f.read(50))  # Reads the first 50 characters
    # print(f.read(50))  # Reads the next 50 characters
    
    # print(f.readline(10))  # Reads the first 10 characters of the line
    # print(f.readline())  # Reads the remainder of the first line in a new line
    # for i in range(1, 5): 
        # print(f.readline())

    # print(f.readlines(1))
    # print(f.readlines(1))
    # print(f.readlines(10))
    # print(f.readlines(10))
    # print(f.readlines(100))
    # print(f.readlines(-1))

    read_50 = print(f.read(50))
    loop_readline = []
    for i in range(1, 5): 
        loop_readline.append(f.readline())
    readlines_100 = print(f.readlines(100))

print(f'''
First 50 characters: {read_50}
Next four line, as list by line: {loop_readline}
Next 100 characters, as list by line, and rounded up to complete lines": {readlines_100}
''')

