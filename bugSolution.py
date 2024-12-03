def function_with_improved_error_handling(a, b):
    if not isinstance(b,(int, float)):
        return "Error: Denominator must be a number"
    try:
        if isinstance(a,(int, float)) and isinstance(b,(int, float)):
            result = a / b
            return result
        else:
            return "Error: Invalid input type for numerator and denominator"
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"An unexpected error occurred: {type(e).__name__}, {e}"

# Example usage:
print(function_with_improved_error_handling(10, 2))  # Output: 5.0
print(function_with_improved_error_handling(10, 0))  # Output: Error: Division by zero
print(function_with_improved_error_handling(10, "abc")) # Output: Error: Denominator must be a number
print(function_with_improved_error_handling(10, [1,2])) # Output: Error: Denominator must be a number
print(function_with_improved_error_handling("ten", 2)) # Output: Error: Invalid input type for numerator and denominator