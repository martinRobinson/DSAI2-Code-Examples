from city_functions1 import city_country


def test_city_country():
    """Does a simple city and country pair work?"""
    test_city = city_country("dublin", "ireland")
    assert test_city == "Dublin, Ireland"
