class Employee:
    """Show  employee first name, last name and annual salary."""

    def __init__(self, first_name, last_name, annual_salary):
        """initialize  employee required data."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, annual_raise=5000):
        """adds $5,000 to the annual salary by default but also accepts a different raise amount."""
        self.annual_salary += annual_raise
        
