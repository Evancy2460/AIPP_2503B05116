def classify_age(age: int) -> str:
    # Nested if-elif-else classification
    if age >= 0:
        if age < 3:
            return "Infant"
        elif age < 13:
            return "Child"
        else:
            if age < 20:
                return "Teenager"
            elif age < 60:
                return "Adult"
            else:
                return "Senior"
    else:
        return "Invalid age"


if __name__ == "__main__":
    try:
        value = int(input("Enter age: "))
    except ValueError:
        print("Invalid age")
    else:
        print(classify_age(value))

