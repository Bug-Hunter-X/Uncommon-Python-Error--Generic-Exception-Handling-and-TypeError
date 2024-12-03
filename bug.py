def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid input type"
except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage:
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Division by zero
print(function_with_uncommon_error(10, "abc")) # Output: Error: Invalid input type
print(function_with_uncommon_error(10, [1,2])) # Output: Error: unsupported operand type(s) for /: 'int' and 'list'