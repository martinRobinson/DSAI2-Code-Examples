def names_to_upper_case(names):
    for i in range(0, len(names)):
        names[i] = names[i].upper()


people = ["tom", "dick", "harry", "mary"]
print("People before function call: ", people)
names_to_upper_case(people)
print("People after function call: ", people)
