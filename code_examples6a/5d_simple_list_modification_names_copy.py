def names_to_upper_case(names):
    copy_names = names.copy()
    for i in range(0, len(names)):
        copy_names[i] = names[i].upper()

    return copy_names


people = ["tom", "dick", "harry", "mary"]
print("People before function call:", people)
people_uppercase = names_to_upper_case(people)
print("People after function call:", people)
print("People upper case after function", people_uppercase)
