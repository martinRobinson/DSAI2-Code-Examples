class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.domain = "atu.ie"
        self.username = self.create_username(first_name, last_name)
        self.email = self.create_email(self.username, self.domain)
        self.location = location.title()
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


joseph = User("joseph", "bloggs", "ramelton")
joseph.describe_user()
joseph.greet_user()
print("\nMaking 3 login attempts...")
joseph.increment_login_attempts()
joseph.increment_login_attempts()
joseph.increment_login_attempts()
print(f"User {joseph.username} - Login attempts: {joseph.login_attempts}")


marie = User("marie", "curie", "letterkenny")
marie.describe_user()
marie.greet_user()
print("\nMaking 3 login attempts...")
marie.increment_login_attempts()
marie.increment_login_attempts()
marie.increment_login_attempts()
print(f"User {marie.username} - Login attempts: {marie.login_attempts}")
