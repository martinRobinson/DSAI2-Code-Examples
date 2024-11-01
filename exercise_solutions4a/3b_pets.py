# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'hamster',
    'name': 'tiny',
    'owner': 'margaret',
    'weight': 1.2,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'tiger',
    'name': 'mauler',
    'owner': 'beatrice',
    'weight': 124,
    'eats': 'meat',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'tatters',
    'owner': 'stephen',
    'weight': 23,
    'eats': 'shoes',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
