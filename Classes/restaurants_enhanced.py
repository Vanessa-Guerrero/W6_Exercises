class Restaurant:
    '''Class (blueprint) to describe a restaurant'''
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = [] 

    # Method to describe the restaurant
    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}.')

    # Method to indicate if the restaurant is open
    def rest_open(self):
        print(f'{self.rest_name} is open.')

    def add_num_served(self):
        how_many_cust = int(input(f'How many customers served today for {self.rest_name}? '))
        self.number_served += how_many_cust

    def print_num_served(self):
        print(f'{self.rest_name} has served {self.number_served} customers\n')

    def customer_rating(self):
        rate = int(input(f'How would you rate your experience today at {self.rest_name} on a scale of 1-5 (5 being excellent)? '))
            
        if 1 <= rate <= 5: 
            self.customer_ratings.append(rate)
            avg_rate = sum(self.customer_ratings)/len(self.customer_ratings)
            print(f'Your rating was {rate}. The average rating for this restaurant is {avg_rate} \n')
        else:
            print("Error! Please enter a number between 1 and 5.")

# Create three instances of the Restaurant class with different restaurant details
Weedys = Restaurant("Weedy's", "Hurgusburgus")
Sbubby = Restaurant("Sbubby", "Freef Sandwiches")
Donkin = Restaurant("Donkin' Dunnts", "Dundun Coffee")

# Calling the methods on each instance to test the output
Weedys.describe_rest()
Weedys.rest_open()
Weedys.add_num_served()
Weedys.print_num_served()
Weedys.customer_rating()

Sbubby.describe_rest()
Sbubby.rest_open()
Sbubby.add_num_served()
Sbubby.print_num_served()
Sbubby.customer_rating()

Donkin.describe_rest()
Donkin.rest_open()
Donkin.add_num_served()
Donkin.print_num_served()
Donkin.customer_rating()
