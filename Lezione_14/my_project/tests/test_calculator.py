from my_project.calculator import Calculator
import pytest

@pytest.fixture
def calcutaion():
    # creates a fresh instance of Calculator before each test
    return Calculator(10,5)

def test_addition():
    calculation: Calculator = Calculator(10,5)
    assert calculation.addition() == 13, "The sum is wrong"

def test_subtraction():
    calculation: Calculator = Calculator(10,5)
    assert calculation.subtraction() == 13, "The subtraction is wrong"

def test_multiplication():
    calculation: Calculator = Calculator(10,5)
    assert calculation.multiplication() == 50, "The multiplication is wrong"

def tesst_division():
    calculation: Calculator = Calculator(10,5)
    assert calculation.division() == 2.00, "The quotient is wrong"