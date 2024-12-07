def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid input type")
        return None

# Correct way to handle lists as arguments
list_a = [10, 20]
list_b = [2, 0]
for i in range(len(list_a)):
    try:
      result = list_a[i] / list_b[i]
      print(f"Result: {result}")
    except ZeroDivisionError:
      print(f"Error: Cannot divide by zero at index: {i}")
    except TypeError:
      print(f"Error: Invalid input types at index {i}")

# More robust exception handling
def another_uncommon_error(a,b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return 0 #Return default value to prevent further errors
    except TypeError:
        print("Error: Invalid input types")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None #Handle other unexpected exceptions