#!/usr/bin/env python3
"""Assignment 1 — list operations

Provides a function to find the largest number in a user-provided list.
"""

def find_largest(numbers: list[float]) -> float:
    """Return the largest number in the given list.
    
    Args:
        numbers: non-empty list of numbers
        
    Returns:
        The largest number in the list
        
    Raises:
        ValueError: if the list is empty
    """
    if not numbers:
        raise ValueError("Cannot find largest in empty list")
    return max(numbers)


if __name__ == "__main__":
    print("Enter numbers one per line. Leave blank when done.")
    numbers = []
    
    try:
        while True:
            line = input("Enter number (or blank to finish): ").strip()
            if line == "":
                break
                
            try:
                num = float(line)
                numbers.append(num)
            except ValueError:
                print(f"'{line}' is not a valid number, try again.")
                continue
                
        if numbers:
            largest = find_largest(numbers)
            print(f"\nYour numbers: {numbers}")
            print(f"Largest number: {largest}")
        else:
            print("\nNo numbers entered.")
            
    except (KeyboardInterrupt, EOFError):
        print("\nInput cancelled.")
    print("Goodbye.")
