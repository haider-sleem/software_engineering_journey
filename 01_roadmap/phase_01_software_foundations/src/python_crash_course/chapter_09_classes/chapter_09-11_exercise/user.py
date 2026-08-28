"""Classes used to represent users and administrators with their privileges."""


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


class Privileges:
    """shows the privileges of an admin."""

    def __init__(self, privileges):
        """Inintializes admins privileges as a list."""
        self.privileges = privileges

    def show_privileges(self):
        """shows the privileges of the admin."""
        if len(self.privileges) > 1:
            print(
                f"The Admin privileges are: {', '.join(self.privileges[:-1])} and {self.privileges[-1]}."
            )
        elif len(self.privileges) == 1:
            print(f"The Admin privilege is: {''.join(self.privileges)}.")
        else:
            print("No privileges to show.")


class Admin(User):
    """shows a special kind of user."""

    def __init__(self, first_name, last_name, age, job, privileges):
        super().__init__(first_name, last_name, age, job)
        self.privileges = Privileges(privileges)
