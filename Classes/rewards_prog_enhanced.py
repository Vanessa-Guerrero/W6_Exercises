cust_list = [] # creating a global variable to use later

# Defining my class RewardsProgram
class RewardsProgram:
    '''Describes customer information for the rewards program'''
    
    # Initialize the customer with their name, phone, and email
    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
        self.restaurants_visited = []
        self.rewards_points = 0
        
    # Method to display the customer's profile
    def profile(self):
        print(f'Name: {self.cust_name}')
        print(f'Phone: {self.phone}')
        print(f'Email: {self.email}')
    
    # Method to thank the customer for visiting
    def thank_you(self):
        print(f'Thank you, {self.cust_name}, for visiting our restaurant!\n')

    # Method to add the customer's information to the global variable cust_list
    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))

    # New method to track restaurant visits and add rewards points
    def visit_rest(self):
        # Prompt for the name of the restaurant
        restaurant_name = input("Name of restaurant: ").strip()
        
        # Check if the restaurant has already been visited
        if restaurant_name not in self.restaurants_visited:
            # Add the restaurant to the visited list
            self.restaurants_visited.append(restaurant_name)

        # Prompt for total food bill and converting it to points (1 dollar = 1 point)
        food_bill = round(int(input('What was the total food bill for this visit? $ ')))
        self.rewards_points += food_bill

        # Display results for method
        print(f'Points for this visit: {food_bill}')
        print(f'Total rewards points earned: {self.rewards_points}')
        print(f'Thank you for visiting {restaurant_name}!')





# Create three instances of the RewardsProgram class with sample data
customer1 = RewardsProgram("Jane Doe", "555-1234", "Jane@email.com")
customer2 = RewardsProgram("John Smith", "555-5678", "John@email.com")
customer3 = RewardsProgram("Charlie Brown", "555-8765", "charlie@email.com")

# Running the new method for each customer
customer1.visit_rest()

customer2.visit_rest()

customer3.visit_rest()
