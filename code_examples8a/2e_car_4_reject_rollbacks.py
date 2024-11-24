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
        """
        Set the milometer reading to the given value.
        Reject the change if it attempts to roll the milometer back.
        """
        if mileage >= self.milometer_reading:
            self.milometer_reading = mileage
        else:
            print("You can't roll back an milometer!")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_milometer(23)
my_new_car.read_milometer()

my_new_car.update_milometer(10)
my_new_car.read_milometer()
