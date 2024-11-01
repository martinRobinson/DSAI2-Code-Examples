def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type = 'tiger', pet_name = 'tommy')
describe_pet(animal_type = 'hamster', pet_name = 'rex')
describe_pet(animal_type = 'wolf', pet_name = 'rover')
