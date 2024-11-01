# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'joseph',
    'last_name': 'bloggson',
    'age': 25,
    'city': 'lifford',
    }
people.append(person)

person = {
    'first_name': 'michael',
    'last_name': 'smith',
    'age': 20,
    'city': 'ramelton',
    }
people.append(person)

person = {
    'first_name': 'mary',
    'last_name': 'green',
    'age': 34,
    'city': 'milford',
    }
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name}, of {city}, is {age} years old.")
