class Restaurant:
    """An attempt to model a restaurant."""

    def __init__(self, rest_name, food_type):
        """Initialize restaurant name and food type attributes."""
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        """Print a statement describing the restaurant."""
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        """Print a message stating the restaurant is open."""
        print(f"{self.rest_name} is open.")

# Create three different restaurant instances
restaurant1 = Restaurant('The Binkle', 'Tacos')
restaurant2 = Restaurant('Weedy\'s', 'Old Fashioned HurgusBurgus')
restaurant3 = Restaurant('Applebapple\'s', 'Nehhborhor Grib & Bib')

# Call describe_rest() and rest_open() for each instance
restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()