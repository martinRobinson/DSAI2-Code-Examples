def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('tiger', 'tommy')
describe_pet('hamster', 'rex')
describe_pet('wolf', 'rover')
