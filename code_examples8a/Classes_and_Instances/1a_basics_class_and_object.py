# Create an empty class
class Employee:
    pass

# Instantiate two objects from the class
employee1 = Employee()
employee2 = Employee()

# Print the two employee objects.
print(employee1)
print(employee2)

# Directly set instance variables for the two employees
employee1.first_name = 'joe'
employee1.last_name = 'bloggs'
employee1.email = 'joe@atu.ie'
employee1.pay = 50000

employee2.first_name = 'marie'
employee2.last_name = 'curie'
employee2.email = 'marie@atu.ie'
employee2.pay = 65000

print(employee1.email)
print(employee2.email)
