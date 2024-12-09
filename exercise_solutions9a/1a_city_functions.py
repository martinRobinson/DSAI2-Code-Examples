"""A collection of functions for working with cities."""


def city_country(city, country):
    """Return a string like 'Dublin, Ireland'."""
    return f"{city.title()}, {country.title()}"
