class Restaurant:
    """An attempt to model a restaurant."""

    def __init__(self, rest_name, food_type):
        """Initialize restaurant name and food type attributes."""
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        """Print a statement describing the restaurant."""
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        """Print a message stating the restaurant is open."""
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        """Add the number of customers served to the total."""
        while True:
            try:
                customers_served = int(input("How many customers served today? "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        self.number_served += customers_served

    def print_num_served(self):
        """Print the number of customers served."""
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        """Accept and record customer ratings, and calculate the average rating."""
        while True:
            try:
                rating = int(input("How would you rate your experience today on a scale of 1-5 (5 being excellent)? "))
                if 1 <= rating <= 5:
                    break
                else:
                    print("Invalid input. Please enter an integer between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        self.customer_ratings.append(rating)
        if len(self.customer_ratings) > 0:
            average_rating = sum(self.customer_ratings) / len(self.customer_ratings)
            print(f"Your rating was {rating}. The average rating for this restaurant is {average_rating:.2f}")
        else:
            print(f"Your rating was {rating}. No average rating available yet.")

# Create three different restaurant instances
restaurant1 = Restaurant('The Binkle', 'Tacos')
restaurant2 = Restaurant('Weedy\'s', 'Old Fashioned HurgusBurgus')
restaurant3 = Restaurant('Applebapple\'s', 'Nehhborhor Grib & Bib')


class FoodTruck(Restaurant):
    """A simple attempt to model a food truck, inheriting from Restaurant."""

    def __init__(self, rest_name, food_type):
        """
        Initialize attributes for the food truck.
        """
        super().__init__(rest_name, food_type)
        self.private_bookings = 'N'
        self.truck_location = ''
        self.location_history = []  # To store the history of locations

    def accepts_private_bookings(self):
        """Update whether the food truck accepts private bookings."""
        self.private_bookings = input("Does this food truck accept private bookings? Y/N: ").upper()
        if self.private_bookings == 'Y':
            print("This food truck currently accepts private bookings.")
        else:
            print("This food truck currently does not accept private bookings.")

    def relocate_truck(self):
        """Update the food truck's location and store it in the location history."""
        address = input("Enter the truck's current street address: ")
        city = input("Enter the truck's current city: ")
        self.truck_location = f"{address}, {city}"
        self.location_history.append(self.truck_location)  # Add location to history
        print(f"Truck is currently located at {self.truck_location}")

    def print_location_history(self):
        """Print the history of locations for the food truck."""
        print(f"Location history for {self.rest_name}:")
        if self.location_history:
            for location in self.location_history:
                print(location)
        else:
            print("No location history available.")

# Create a food truck instance
my_food_truck = FoodTruck('Inoot-Ut-Brubge', 'Brubge')

# Test the FoodTruck methods
my_food_truck.accepts_private_bookings()
my_food_truck.relocate_truck()
my_food_truck.relocate_truck()  # Relocate the truck again to add another location
my_food_truck.print_location_history()