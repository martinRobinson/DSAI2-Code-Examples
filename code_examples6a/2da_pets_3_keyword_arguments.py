def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name = 'tommy', animal_type = 'tiger')
describe_pet(animal_type = 'hamster', pet_name = 'rex')
describe_pet(pet_name = 'rover', animal_type = 'wolf')
