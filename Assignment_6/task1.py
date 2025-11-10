class Student:
    def __init__(self, name: str, roll_number: int, grade: str) -> None:
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def display_details(self) -> str:
        return f"Student(name='{self.name}', roll_number={self.roll_number}, grade='{self.grade}')"


if __name__ == "__main__":
    # Quick check for expected output
    student = Student("Alice", 101, "A")
    print(student.display_details())

