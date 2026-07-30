from user import User


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
