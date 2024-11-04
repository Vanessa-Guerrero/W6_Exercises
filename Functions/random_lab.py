import random

rand_int = random.randint(0,25)
print(rand_int)                     # printing a random integer from 0 to 25

rand = random.random()
print(rand)                         # printing a random float value from 0.0 to 1.0 

fruits = ["apple", "banana", "cherry", "peach", "plum", "watermelon"] 
print(random.choice(fruits))        # printing a random value from fruits list

# printing a random value as a list, optional to specify how many I want and weight of value
print(random.choices(fruits)) 
print(random.choices(fruits, k = 10)) # specifying to print 10 random choices

# in addition to 10 choices, I specified to add 2 apples, 2 bananas, 3 peaches etc (need to add weight for all values if you choose to specify weight)
print(random.choices(fruits, weights = [2,2,1,3,1,1] , k = 10)) 

# printing a random sequence of values in list, needing to specifying how many w/o exceeding length of the og sequence
print(random.sample(fruits, k = 4))  

# print(random.shuffle(fruits)) 
# can't do this since this method changes the og list so I need to do it before printing without changing the variable

random.shuffle(fruits)  # reorganizes the list
print(fruits)           