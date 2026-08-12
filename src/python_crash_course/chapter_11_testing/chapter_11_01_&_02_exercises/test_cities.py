from city_functions import city_country


def test_city_country():
    """Makes sure the function city_country works."""
    function_result1 = city_country("cairo", "egypt")
    assert function_result1 == "Cairo, Egypt"

def test_city_country_population():
    """Makes sure the function city_country populations works."""
    function_result2 = city_country("santiago", "chile", 5000000)
    assert function_result2 == "Santiago, Chile - population 5000000"
