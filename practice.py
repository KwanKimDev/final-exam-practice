"""
# Question 1
def lists_division(x, y):
    sum_x = sum(x)
    sum_y = sum(y)

    return sum_y / sum_x


# Example usage:
x_values = [10, 20, 30]
y_values = [5, 10, 15]
result = lists_division(x_values, y_values)
print("Result:", result)
"""

# Question 2
# Make the version of the code object oriented. Thus, transform the code to have a class ListCalculator, which has two instance variables (x and y, both lists of integers) and lists division as a method. Add a constructor for this class, which sets the two lists, and update the lists_division method to use the instance variables instead of the function parameters. Commit this version of the code. Try to run it to make sure everything works


class ListCalculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def lists_division(self):
        sum_x = sum(self.x)
        sum_y = sum(self.y)
        return sum_y / sum_x


x_values = [10, 20, 30]
y_values = [5, 10, 15]
calculator = ListCalculator(x_values, y_values)
result = calculator.lists_division()
print("Result:", result)

"""
# Question 3
# Add at least two unit tests for the ListCalculator class to test the lists_division method. If you did not manage to have a solution for exercise 2, create two unit tests for the sample code in exercise 1. Keep the test code as a separate file and call it TestListCalculator.py Remember that this file should import the code under test e.g.from practice import ListCalculator Add the tests and commit this version of the code.

import unittest
from practice import ListCalculator


class ListCalculatorTest(unittest.TestCase):
    def testsame(self):
        x_values = [2, 4, 6]
        y_values = [2, 4, 6]
        calculator = ListCalculator(x_values, y_values)
        result = calculator.lists_division()
        self.assertEqual(result, 1)

    def testnegative(self):
        x_values = [-10, -20, -30]
        y_values = [5, 10, 15]
        calculator = ListCalculator(x_values, y_values)
        result = calculator.lists_division()
        self.assertEqual(result, -0.5)

    def testseveral(self):
        x_values = [10, 20, 30, 40]
        y_values = [5, 10, 15, 20]
        calculator = ListCalculator(x_values, y_values)
        result = calculator.lists_division()
        self.assertEqual(result, 0.5)

    def testfew(self):
        x_values = [10]
        y_values = [5]
        calculator = ListCalculator(x_values, y_values)
        result = calculator.lists_division()
        self.assertEqual(result, 0.5)


if __name__ == "__main__":
    unittest.main()
"""

# Question 4
# Add a test where your inputs for lists_division  are: y = [3,5,7] and x = [5,-4,-1] Do not add any assertion in this test case What happens when you run the test? Use the debugger to explain the issue Create screenshots and add them to the readme file on github.com directly.

import unittest
from practice import ListCalculator


class ListCalculatorTest(unittest.TestCase):
    def question4(self):
        x_values = [5, -4, -1]
        y_values = [3, 5, 7]
        calculator = ListCalculator(x_values, y_values)
        result = calculator.lists_division()
        return result
