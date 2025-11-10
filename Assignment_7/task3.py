#Debug the following code
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Both inputs must be numbers.")
        return None

try:
    print(divide(10, 0))
except Exception as e:
    print(f"Unexpected error: {e}")