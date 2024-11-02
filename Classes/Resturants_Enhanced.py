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

# Test the new methods for each restaurant
restaurants = [restaurant1, restaurant2, restaurant3]
for restaurant in restaurants:
    print(f"\n--- {restaurant.rest_name} ---")
    restaurant.print_num_served()
    restaurant.add_num_served()
    restaurant.add_num_served()
    restaurant.print_num_served()

    restaurant.customer_rating()
    restaurant.customer_rating()
    restaurant.customer_rating()