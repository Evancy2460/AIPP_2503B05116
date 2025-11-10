_AGE_UPPER_BOUNDS = [-1, 2, 12, 19, 59]
_AGE_LABELS = ["Invalid age", "Infant", "Child", "Teenager", "Adult", "Senior"]


def classify_age(age: int) -> str:
    # Classify using match-case (Python's switch) without if/elif/else
    index = sum(age > bound for bound in _AGE_UPPER_BOUNDS)
    match index:
        case 0:
            return "Invalid age"
        case 1:
            return "Infant"
        case 2:
            return "Child"
        case 3:
            return "Teenager"
        case 4:
            return "Adult"
        case _:
            return "Senior"


if __name__ == "__main__":
    try:
        value = int(input("Enter age: "))
        print(classify_age(value))
    except ValueError:
        print("Invalid age")


