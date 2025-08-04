def safe_divide(numerator, denominator):
    """Safely divide two numbers, handling errors for zero division and non-numeric input."""
    try:
        # Convert to float first
        num = float(numerator)
        denom = float(denominator)
        
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."

