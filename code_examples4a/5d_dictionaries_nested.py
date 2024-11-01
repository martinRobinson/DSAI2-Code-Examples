employee_details = {
    'employee1': {'name': 'Martin', 'salary': 7500},
    'employee2': {'name': 'Joseph', 'salary': 8000},
    'employee3': {'name': 'Mary', 'salary': 5000}
}

for employee,details in employee_details.items():
    print(employee, details['name'], details['salary'])

# Give Mary a payrise.
employee_details['employee3']['salary'] = 9000

print()

for employee,details in employee_details.items():
    print(employee, details['name'], details['salary'])



