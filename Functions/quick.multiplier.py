# Create the lambda function that doubles the argument
doubler = lambda n: n * 2

# lambda function that triples argument
tripler = lambda n: n * 3

# Defining a function for multipliers 4-10
def multiplier(n):
    return lambda x: x * n

# Creating the multiplier variables
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

# My test values for the multipliers
test_values = [8, -4, 'banana']

# Loop through each test value, apply the corresponding lambda function, and print results
for value in test_values:
    print(f"Doubler({value}): {doubler(value)}")
    print(f"Tripler({value}): {tripler(value)}")
    print(f"Quadrupler({value}): {quadrupler(value)}")
    print(f"Quintupler({value}): {quintupler(value)}")
    print(f"Sextupler({value}): {sextupler(value)}")
    print(f"Septupler({value}): {septupler(value)}")
    print(f"Octupler({value}): {octupler(value)}")
    print(f"Nonupler({value}): {nonupler(value)}")
    print(f"Decupler({value}): {decupler(value)}\n")