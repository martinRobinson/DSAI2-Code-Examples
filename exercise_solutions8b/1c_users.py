class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.domain = "atu.ie"
        self.username = self.create_username(first_name,last_name)
        self.email = self.create_email(self.username, self.domain)
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")
    
    def create_username(self, first_name, last_name):
        username = f"{first_name[0]}_{last_name}"
        return username

    def create_email(self, username, domain):
        email = f"{username}@{domain}"
        return email

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

joseph = User('joseph', 'bloggs', 'ramelton')
joseph.describe_user()
joseph.greet_user()

marie = User('marie', 'curie', 'letterkenny')
marie.describe_user()
marie.greet_user()
