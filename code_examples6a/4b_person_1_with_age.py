def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('ed', 'sheeran', age=27)
print(musician)

musician = build_person('suzanne', 'vega')
print(musician)

