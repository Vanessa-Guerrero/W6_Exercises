# Handling ValueError
try:
    x = int(input("Please add a # "))
except ValueError:
    print("ValueError: Not a valid #, please try again")
else:
    print(x)
finally:
    print("Let's try another one...")

# Handling NameError
try:
    name = 'Vanessa'
    print(myname)
except NameError:
    print("NameError: Oops, try again. Looks like you tried to call an undefined variable")
else:
    print(name)
finally:
    print("Let's try another one...")

# Handling SyntaxError
try:
   x === 4
except SyntaxError:
    print("SyntaxError: You used invalid Python syntax. Try again")
else:
    print(x)
finally:
    print("Let's try another one...")
