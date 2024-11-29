"""A collection of classes for modeling users."""


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


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, location)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Privileges:
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")
