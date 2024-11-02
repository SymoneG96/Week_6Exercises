cust_list = []

class RewardsProgram:
    """An attempt to model a restaurant rewards program."""

    def __init__(self, cust_name, phone, email):
        """Initialize customer information attributes."""
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
        self.restaurants_visited = []
        self.rewards_points = {}  # Use a dictionary to track points per restaurant

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

    def visit_rest(self):
        """Record a restaurant visit and calculate rewards points."""
        restaurant_name = input("Name of restaurant: ")
        if restaurant_name not in self.restaurants_visited:
            self.restaurants_visited.append(restaurant_name)

        while True:
            try:
                bill_amount = float(input("What was the total food bill for this visit? $"))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the bill amount.")

        points_earned = self.calculate_rewards(bill_amount)

        if restaurant_name in self.rewards_points:
            self.rewards_points[restaurant_name] += points_earned
        else:
            self.rewards_points[restaurant_name] = points_earned

        print(f"Points for this visit: {points_earned}")
        print(f"Total rewards points earned: {self.rewards_points[restaurant_name]}")
        print(f"Thank you for visiting {restaurant_name}!")

    def calculate_rewards(self, bill_amount):
        """Calculate rewards points based on the bill amount."""
        return int(bill_amount)  # $1 = 1 point, rounded down


# Create three different customer instances
customer1 = RewardsProgram('Diana Ross', '312-555-1212', 'diana@motown.com')
customer2 = RewardsProgram('Beetle Juice', '404-555-3333', 'beetlejuice@netherworld.net')
customer3 = RewardsProgram('Mr. Krabs', '907-555-9999', 'krabs@krustykrab.com')

# Example usage with visit_rest()
customer1.visit_rest()  
customer1.visit_rest()  # Visit the same restaurant again to see points accumulate