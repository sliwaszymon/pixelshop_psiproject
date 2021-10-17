import zad5 as Model

class ScienceCalculator(Model.Calculator):
    """Science calculator, with all methods from Calculator class."""

    def exp(a, b):
        """Return a to power of b."""
        return a ** b

    def factorial(a):
        """Return the factorial of a."""
        factorial = 1
        for x in range(1,a+1,1):
            factorial = factorial * x
        return factorial

    def mod(a, b):
        """Return a modulo b."""
        return a % b


print(ScienceCalculator.add(1,2,3,4,5,6,7))
print(ScienceCalculator.difference(1,3))
print(ScienceCalculator.multipy(2,3))
print(ScienceCalculator.divide(3,5))
print(ScienceCalculator.exp(2,8))
print(ScienceCalculator.factorial(5))
print(ScienceCalculator.mod(5,3))