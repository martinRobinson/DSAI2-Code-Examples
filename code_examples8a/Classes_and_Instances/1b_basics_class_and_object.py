# Create an empty class
class Employee:

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = f"{firstname}@atu.ie"

# Instantiate two objects from the class
employee1 = Employee('joe', 'bloggs', 50000)
employee2 = Employee('marie', 'curie', 65000)

print("Accessing employee attributes directly:")
print(employee1.email)
print(employee2.email)
