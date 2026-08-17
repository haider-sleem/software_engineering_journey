import pytest
from employee import Employee


def test_give_default_raise():
    """A test gives default raise."""
    employee = Employee("Ali", "Sleem", 50000)
    employee.give_raise()
    assert employee.annual_salary == 55000


def test_give_custom_raise():
    """A  test gives custom raise."""
    employee = Employee("Ali", "Sleem", 50000)
    employee.give_raise(10000)
    assert employee.annual_salary == 60000


#### Part 2


# @pytest.fixture
# def employee():
#     """An employee data that will be available to all test functions."""
#     employee = Employee("Ali", "Sleem", 50000)
#     return employee


# def test_give_default_raise(employee):
#     """A test gives default raise."""
#     employee.give_raise()
#     assert employee.annual_salary == 55000


# def test_give_custom_raise(employee):
#     """A  test gives custom raise."""
#     employee.give_raise(10000)
#     assert employee.annual_salary == 60000
