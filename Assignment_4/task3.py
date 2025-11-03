def format_name(first_name, last_name):
    """
    Format full name as 'Last, First'.
    
    Args:
        first_name (str): First name of the person
        last_name (str): Last name of the person
        
    Returns:
        str: Formatted name as 'Last, First'
    """
    # Strip any extra whitespace and capitalize first letter of each name
    first_name = first_name.strip().capitalize()
    last_name = last_name.strip().capitalize()
    
    return f"{last_name}, {first_name}"

# Taking input from keyboard in a loop
if __name__ == "__main__":
    while True:
        print("\nEnter names to format (or press Enter twice to exit)")
        
        # Get first name
        first_name = input("Enter first name: ").strip()
        if not first_name:  # Check for empty input
            print("Thank you for using the name formatter!")
            break
            
        # Get last name
        last_name = input("Enter last name: ").strip()
        if not last_name:  # Check for empty input
            print("Thank you for using the name formatter!")
            break
        
        # Format and display the result
        formatted_name = format_name(first_name, last_name)
        print(f"\nFormatted name: {formatted_name}")
