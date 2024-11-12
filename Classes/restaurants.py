class Restaurant:
    '''Class (blueprint) to describe a restaurant'''
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    # Method to describe the restaurant
    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}.')

    # Method to indicate if the restaurant is open
    def rest_open(self):
        print(f'{self.rest_name} is open.\n')

# Create three instances of the Restaurant class with different restaurant details
Weedys = Restaurant("Weedy's", "Hurgusburgus")
Sbubby = Restaurant("Sbubby", "Freef Sandwiches")
Donkin = Restaurant("Donkin' Dunnts", "Dundun Coffee")

# Calling the methods on each instance to test the output
Weedys.describe_rest()
Weedys.rest_open()

Sbubby.describe_rest()
Sbubby.rest_open()

Donkin.describe_rest()
Donkin.rest_open()

