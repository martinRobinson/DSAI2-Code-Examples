def describe_pet(pet_name, animal_type=None):
    """Display information about a pet."""
    if animal_type is None:
        print(f"My pet's name is {pet_name.title()}")
    else:
        print(f"I have a {animal_type}.")
        print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name="tommy")
describe_pet(animal_type="hamster", pet_name="rex")
describe_pet(pet_name="rover")
