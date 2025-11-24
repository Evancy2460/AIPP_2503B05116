def compute_statistics(students_marks):
    if not students_marks:
        return None, []
    
    mean = sum(students_marks.values()) / len(students_marks)
    above_mean = [name for name, marks in students_marks.items() if marks > mean]
    
    return mean, above_mean


if __name__ == "__main__":
    while True:
        students_marks = {}
        
        num_students = int(input("Enter the number of students (or 0 to exit): "))
        
        if num_students == 0:
            print("Exiting...")
            break
        
        for i in range(num_students):
            marks = float(input(f"Enter marks for student {i+1}: "))
            students_marks[f"Student {i+1}"] = marks
        
        mean, above_mean = compute_statistics(students_marks)
        
        print(f"\nMean: {mean:.2f}")
        print(f"Students above mean: {above_mean}\n")
