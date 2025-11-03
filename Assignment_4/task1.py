def is_leap_year(year):
    """
    Check if a given year is a leap year.
    
    Args:
        year (int): The year to check
    
    Returns:
        bool: True if the year is a leap year, False otherwise
    """
    # A year is a leap year if:
    # 1. It's divisible by 4 AND
    # 2. Either:
    #    a) It's NOT divisible by 100 OR
    #    b) It's divisible by 400
    
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False

# Taking input from keyboard in a loop
if __name__ == "__main__":
    while True:
        try:
            # Get year input from user
            print("\nEnter a year to check if it's a leap year")
            print("(Enter 0 or a negative number to exit)")
            year = int(input("Year: "))
            
            # Check if user wants to exit
            if year <= 0:
                print("Thank you for using the leap year checker!")
                break
            
            # Check if it's a leap year
            result = is_leap_year(year)
            
            # Display the result
            print(f"{year} is{' ' if result else ' not '}a leap year")
            
        except ValueError:
            print("Please enter a valid year (integer number)")
