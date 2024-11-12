cust_list = [] # creating a global variable to use later

# Defining my class RewardsProgram
class RewardsProgram:
    '''Describes customer information for the rewards program'''
    
    # Initialize the customer with their name, phone, and email
    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
    
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


# Create three instances of the RewardsProgram class with sample data
customer1 = RewardsProgram("Jane Doe", "555-1234", "Jane@email.com")
customer2 = RewardsProgram("John Smith", "555-5678", "John@email.com")
customer3 = RewardsProgram("Charlie Brown", "555-8765", "charlie@email.com")

# Run the methods for each customer
customer1.profile()
customer1.thank_you()
customer1.add_to_cust_list()

customer2.profile()
customer2.thank_you()
customer2.add_to_cust_list()

customer3.profile()
customer3.thank_you()
customer3.add_to_cust_list()

# For loop to print customer list 
print("Customer List:")
for customer in cust_list:
    print(customer)