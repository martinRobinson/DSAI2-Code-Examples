from city_functions2 import city_country


def test_city_country():
    """Does a simple city and country pair work?"""
    test_city = city_country("dublin", "ireland")
    assert test_city == "Dublin, Ireland"


def test_city_country_population():
    """Can I include a population argument?"""
    test_city = city_country("dublin", "ireland", population=500_000)
    assert test_city == "Dublin, Ireland - population 500000"

