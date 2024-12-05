from name_function import get_formatted_name


def test_first_last_name():
    """Do names like 'Albert Einstein' work?"""
    formatted_name = get_formatted_name("albert", "einstein")
    assert formatted_name == "Albert Einstein"
