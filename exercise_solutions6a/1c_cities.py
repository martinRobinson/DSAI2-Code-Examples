def describe_city(city, country='ireland'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('dublin')
describe_city('paris', 'france')
describe_city('limerick')
