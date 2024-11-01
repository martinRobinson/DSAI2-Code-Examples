cities = {
    'dublin': {
        'country': 'ireland',
        'population': 900_000,
        'nearby mountains': 'wicklow',
        },
    'glasgow': {
        'country': 'scotland',
        'population': 450_000,
        'nearby mountains': 'trossach',
        },
    'boulder': {
        'country': 'united states',
        'population': 175_000,
        'nearby mountains': 'colarado',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  The {mountains} mountains are nearby.")
