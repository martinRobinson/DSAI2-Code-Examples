# Create an empty class
class Employee:

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = f"{firstname}@atu.ie"

    def full_name(self):
        full_name = f"{self.firstname.title()} {self.lastname.title()}"
        return full_name

# Instantiate two objects from the class
employee1 = Employee('joe', 'bloggs', 50000)
employee2 = Employee('marie', 'curie', 65000)

# Print out the full name of employee1 by accessing 
# instance attributes directly.
print ("Employee details by accessing attributes directly:")
print (f"{employee1.firstname.title()} {employee1.lastname.title()}")

# Print out the full name of employee1 by invoking method.
print ("Employee details by invoking method:")
print(employee1.full_name())
