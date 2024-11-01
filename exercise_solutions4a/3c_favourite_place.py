favorite_places = {
    'joseph': ['dublin', 'paris', 'new york'],
    'michael': ['hamburg', 'los angeles'],
    'mary': ['toyko', 'strabane', 'malin head']
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")
