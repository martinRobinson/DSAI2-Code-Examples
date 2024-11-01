def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"

city = city_country('dublin', 'ireland')
print(city)

city = city_country('london', 'england')
print(city)

city = city_country('glasgow', 'scotland')
print(city)
