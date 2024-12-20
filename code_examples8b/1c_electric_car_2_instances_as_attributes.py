class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.milometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_milometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.milometer_reading} miles on it.")

    def update_milometer(self, mileage):
        """Set the milometer reading to the given value."""
        if mileage >= self.milometer_reading:
            self.milometer_reading = mileage
        else:
            print("You can't roll back an milometer!")

    def increment_milometer(self, miles):
        """Add the given amount to the milometer reading."""
        self.milometer_reading += miles


class Battery:
    """Simple model of a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """Represent aspects of electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
