class Calculator:
    """Util matematical methods."""

    def add(*args):
        """Return sum of args."""
        sum = 0
        for arg in args:
            sum += arg
        return sum

    def difference(a, b):
        """Return difference between a and b."""
        return a - b

    def multipy(a, b):
        """Return multiplication of a and b."""
        return a * b
    
    def divide(a, b):
        """Return the result of the division a by b."""
        return a / b
    

# print(Calculator.add(1,2,3,4,5,6,7))
# print(Calculator.difference(1,3))
# print(Calculator.multipy(2,3))
# print(Calculator.divide(3,5))