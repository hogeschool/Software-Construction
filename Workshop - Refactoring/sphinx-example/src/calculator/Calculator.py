# src/calculator.py

class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.

    This class provides methods to add, subtract, multiply, and divide two numbers.
    """

    def add(self, a, b):
        """
        Add two numbers.

        :param a: The first number.
        :type a: float
        :param b: The second number.
        :type b: float
        :return: The sum of a and b.
        :rtype: float
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtract one number from another.

        :param a: The number to be subtracted from.
        :type a: float
        :param b: The number to subtract.
        :type b: float
        :return: The difference between a and b.
        :rtype: float
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiply two numbers.

        :param a: The first number.
        :type a: float
        :param b: The second number.
        :type b: float
        :return: The product of a and b.
        :rtype: float
        """
        return a * b

    def divide(self, a, b):
        """
        Divide one number by another.

        :param a: The numerator.
        :type a: float
        :param b: The denominator.
        :type b: float
        :return: The quotient of a divided by b.
        :rtype: float
        :raises ZeroDivisionError: If b is zero.
        """
        if b == 0:
            raise ZeroDivisionError("The denominator b cannot be zero.")
        return a / b