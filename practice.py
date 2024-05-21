# Question 1
"""
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

    def divisions(self):
        sum_x = sum(self.x)
        sum_y = sum(self.y)
        return sum_y / sum_x


x_values = [10, 20, 30]
y_values = [5, 10, 15]
calculator = ListCalculator(x_values, y_values)
result = calculator.divisions()
print("Result:", result)
