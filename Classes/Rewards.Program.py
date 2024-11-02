# Create the global cust_list
cust_list = []

class RewardsProgram:
    """A simple attempt to model a restaurant rewards program."""

    def __init__(self, cust_name, phone, email):
        """Initialize customer information attributes."""
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    def profile(self):
        """Print customer's profile information."""
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):
        """Print a thank you message to the customer."""
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):
        """Add the customer's information to the global customer list."""
        customer_info = (self.cust_name, self.phone, self.email)
        cust_list.append(customer_info)

# Create three different customer instances with updated information
customer1 = RewardsProgram('Diana Ross', '312-575-1772', 'diana@motown.com')  # Chicago area code
customer2 = RewardsProgram('Beetle Juice', '404-185-3333', 'beetlejuice@netherworld.net')  # Atlanta area code
customer3 = RewardsProgram('Mr. Krabs', '907-775-9319', 'krabs@krustykrab.com')  # Alaska area code

# Run the methods for each customer
for customer in [customer1, customer2, customer3]:
    customer.profile()
    customer.thank_you()
    customer.add_to_cust_list()
    print("---")

# Print the contents of cust_list
print("Customer List:")
for customer in cust_list:
    print(customer)