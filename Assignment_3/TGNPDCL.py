def calculate_energy_charges(units, customer_type):
    """Calculate energy charges based on units consumed and customer type"""
    if customer_type.upper() == 'DOMESTIC':
        if units <= 100:
            return units * 1.45
        elif units <= 200:
            return (100 * 1.45) + ((units - 100) * 2.60)
        else:
            return (100 * 1.45) + (100 * 2.60) + ((units - 200) * 3.60)
    elif customer_type.upper() == 'COMMERCIAL':
        if units <= 100:
            return units * 3.85
        else:
            return (100 * 3.85) + ((units - 100) * 6.30)
    else:
        return 0

def calculate_fixed_charges(customer_type):
    """Calculate fixed charges based on customer type"""
    if customer_type.upper() == 'DOMESTIC':
        return 25
    elif customer_type.upper() == 'COMMERCIAL':
        return 50
    else:
        return 0

def calculate_customer_charges():
    """Calculate customer charges (flat rate)"""
    return 35

def calculate_electricity_duty(energy_charges):
    """Calculate electricity duty as 6% of energy charges"""
    return energy_charges * 0.06

def print_bill(customer_name, customer_type, previous_reading, current_reading, 
               energy_charges, fixed_charges, customer_charges, electricity_duty, total_bill):
    """Print the formatted bill"""
    units_consumed = current_reading - previous_reading
    print("\n" + "="*50)
    print("           TGNPDCL ELECTRICITY BILL")
    print("="*50)
    print(f"Customer Name: {customer_name}")
    print(f"Customer Type: {customer_type}")
    print(f"Previous Reading: {previous_reading}")
    print(f"Current Reading: {current_reading}")
    print(f"Units Consumed: {units_consumed}")
    print("-"*50)
    print("Charges Breakdown:")
    print(f"Energy Charges (EC): ₹{energy_charges:.2f}")
    print(f"Fixed Charges (FC): ₹{fixed_charges:.2f}")
    print(f"Customer Charges (CC): ₹{customer_charges:.2f}")
    print(f"Electricity Duty (ED): ₹{electricity_duty:.2f}")
    print("-"*50)
    print(f"Total Bill Amount: ₹{total_bill:.2f}")
    print("="*50)

def main():
    # Get customer details
    customer_name = input("Enter Customer Name: ")
    customer_type = input("Enter Customer Type (Domestic/Commercial): ")
    
    # Validate customer type
    while customer_type.upper() not in ['DOMESTIC', 'COMMERCIAL']:
        print("Invalid customer type! Please enter either 'Domestic' or 'Commercial'")
        customer_type = input("Enter Customer Type (Domestic/Commercial): ")
    
    # Get meter readings
    while True:
        try:
            previous_reading = float(input("Enter Previous Unit Reading (PU): "))
            current_reading = float(input("Enter Current Unit Reading (CU): "))
            if current_reading >= previous_reading:
                break
            print("Current reading must be greater than or equal to previous reading!")
        except ValueError:
            print("Please enter valid numerical values for readings!")
    
    # Calculate units consumed
    units_consumed = current_reading - previous_reading
    
    # Calculate various charges
    energy_charges = calculate_energy_charges(units_consumed, customer_type)
    fixed_charges = calculate_fixed_charges(customer_type)
    customer_charges = calculate_customer_charges()
    electricity_duty = calculate_electricity_duty(energy_charges)
    
    # Calculate total bill
    total_bill = energy_charges + fixed_charges + customer_charges + electricity_duty
    
    # Print the bill
    print_bill(customer_name, customer_type, previous_reading, current_reading,
               energy_charges, fixed_charges, customer_charges, electricity_duty, total_bill)

if __name__ == "__main__":
    main()
