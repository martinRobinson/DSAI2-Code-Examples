def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('tommy')
describe_pet(pet_name = 'reggie')
describe_pet('horace', 'hippo')
describe_pet(animal_type = 'hamster', pet_name = 'rex')
describe_pet(pet_name = 'rover', animal_type = 'cow')
