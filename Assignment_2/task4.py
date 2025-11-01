def sum_of_squares(numbers):
    """
    Calculate the sum of squares of numbers in the input list/sequence.
    
    Args:
        numbers: A list or sequence of numbers (int or float)
    
    Returns:
        float: The sum of squares of all numbers
        
    Example:
        >>> sum_of_squares([1, 2, 3])
        14  # 1² + 2² + 3² = 1 + 4 + 9 = 14
    """
    return sum(num * num for num in numbers)


if __name__ == '__main__':
    # Get input from user
    try:
        print("Enter numbers separated by spaces:")
        numbers = [float(x) for x in input().split()]
        result = sum_of_squares(numbers)
        print(f"Sum of squares: {result}")
    except ValueError:
        print("Error: Please enter valid numbers separated by spaces")
