class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        message = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{message}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        message = f"{self.name} is open. Come on in!"
        print(f"\n{message}")

restaurant1 = Restaurant('pats pizzas', 'pizza')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('the chilli shaker', 'curry')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('mr chippie', 'fish and chips')
restaurant3.describe_restaurant()
