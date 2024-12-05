from name_function3 import get_formatted_name


def test_first_last_name():
    """Do names like 'Albert Einstein' work?"""
    formatted_name = get_formatted_name("albert", "einstein")
    assert formatted_name == "Albert Einstein"


def test_first_middle_last_name():
    """Do names like 'Kurt Friedrich Godel' work?"""
    formatted_name = get_formatted_name("kurt", "godel", "friedrich")
    assert formatted_name == "Kurt Friedrich Godel"
