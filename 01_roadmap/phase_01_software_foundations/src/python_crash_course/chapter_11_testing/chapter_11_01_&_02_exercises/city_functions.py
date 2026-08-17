def city_country(city_name, country_name, population=""):
    """Returns formatted city name with its country."""
    if population:
        formatted_name = f"{city_name}, {country_name}"
        return f"{formatted_name.title()} - population {population}"
    else:
        formatted_name = f"{city_name}, {country_name}"
        return formatted_name.title()
