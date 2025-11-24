def factorial(n):
    # REFINEMENT 1: Type Validation - Ensure input is an integer
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    # REFINEMENT 2: Negative Input Handling - Factorial undefined for negatives
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    # REFINEMENT 3 & 4: Edge Cases - Handle 0! = 1 and 1! = 1
    if n == 0 or n == 1:
        return 1
    
    # Calculate factorial iteratively for n >= 2
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter a non-negative integer (or -1 to exit): "))
            if num == -1:
                print("Exiting...")
                break
            result = factorial(num)
            print(f"The factorial of {num} is: {result}\n")
        except ValueError as e:
            print(f"Error: {e}\n")
