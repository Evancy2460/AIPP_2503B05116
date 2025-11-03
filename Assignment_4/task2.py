def cm_to_inches(centimeters):
    """
    Convert centimeters to inches.
    
    Args:
        centimeters (float): Length in centimeters
        
    Returns:
        float: Length in inches (rounded to 2 decimal places)
    """
    CONVERSION_FACTOR = 0.39370079
    return round(centimeters * CONVERSION_FACTOR, 2)

# Taking input from keyboard in a loop
if __name__ == "__main__":
    while True:
        try:
            # Get centimeter input from user
            print("\nEnter length in centimeters to convert to inches")
            print("(Enter 0 or a negative number to exit)")
            cm = float(input("Centimeters: "))
            
            # Check if user wants to exit
            if cm <= 0:
                print("Thank you for using the unit converter!")
                break
            
            # Convert to inches and display result
            inches = cm_to_inches(cm)
            print(f"{cm} centimeters = {inches} inches")
            
        except ValueError:
            print("Please enter a valid number")
