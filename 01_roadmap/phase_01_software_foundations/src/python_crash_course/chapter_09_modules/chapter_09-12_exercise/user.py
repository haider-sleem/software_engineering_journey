class User:
    """define the users first and last name."""

    def __init__(self, first_name, last_name, age, job):
        """Inintializes users first_name,  last_name, age and job."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job

    def describe_user(self):
        """describes all the user available details."""

        print(
            f"The user name is {self.first_name} {self.last_name}, "
            f"he is {self.age} years old, "
            f"and his/her job is {self.job}."
        )

    def greet_user(self):
        """prints personal greetting to the user."""

        print(f"Hello, {self.first_name} {self.last_name}")
