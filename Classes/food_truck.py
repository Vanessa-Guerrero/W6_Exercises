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


# Creating a child class: FoodTruck from parent class: Restaurant
class FoodTruck(Restaurant):
    '''Subclass of Restaurant called FoodTruck'''

    def __init__(self, rest_name, food_type):
        super().__init__(rest_name, food_type)
        self.private_bookings = 'N'
        self.truck_location = ""

    # Method to determine if the truck accepts private bookings
    def accepts_private_bookings(self):
        self.private_bookings = input("Does this food truck accept private bookings? Y/N ").strip().upper()
        if self.private_bookings == 'Y':
            print("This food truck currently accepts private bookings.")
        else:
            print("This food truck does not accept private bookings.")

    # Method to update the truck's location
    def relocate_truck(self):
        self.truck_location = input("Enter the truck’s current location (street address and city): ").strip()
        print(f"Truck is currently located at {self.truck_location}")

# Creating an instance of the FoodTruck class
taco_truck = FoodTruck("Taco Time", "Mexican Street Tacos")

# Testing the FoodTruck methods
taco_truck.describe_rest()            # From parent class
taco_truck.rest_open()                # From parent class
taco_truck.accepts_private_bookings() # Unique to FoodTruck
taco_truck.relocate_truck()           # Unique to FoodTruck