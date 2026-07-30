""" "A class that can be used to represent a restaurant. """

class Restaurant:
    """Represent a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ prints restaurant name and type """
        print(
            f"{'Restaurant':<21}: {self.restaurant_name}\n"
            f"{'Cuisine':<21}: {self.cuisine_type}"
        )

    def open_restaurant(self):
        """ prints a message indicating that the restaurant is open. """
        print(f"{self.restaurant_name} is open.")
