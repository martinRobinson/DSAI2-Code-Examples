def city_country(city, country, population):
    """Return a string like 'Dublin, Ireland - population 500000'."""
    output_string = f"{city.title()}, {country.title()}"
    output_string += f" -population {population}"
    return output_string
