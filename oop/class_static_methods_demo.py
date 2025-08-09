class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers (no class or instance data needed)."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Return the product of two numbers.
        Prints the class attribute 'calculation_type' before calculation.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

