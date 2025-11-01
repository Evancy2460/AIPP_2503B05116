import math
from typing import Union, Optional

Number = Union[int, float]


def circle_area(radius: Number) -> Optional[float]:
    """Calculate the area of a circle."""
    if radius <= 0:
        print("Error: Radius must be positive")
        return None
    return math.pi * radius * radius


def rectangle_area(length: Number, width: Number) -> Optional[float]:
    """Calculate the area of a rectangle."""
    if length <= 0 or width <= 0:
        print("Error: Length and width must be positive")
        return None
    return length * width


def triangle_area(base: Number, height: Number) -> Optional[float]:
    """Calculate the area of a triangle."""
    if base <= 0 or height <= 0:
        print("Error: Base and height must be positive")
        return None
    return 0.5 * base * height


def square_area(side: Number) -> Optional[float]:
    """Calculate the area of a square."""
    if side <= 0:
        print("Error: Side length must be positive")
        return None
    return side * side


def get_positive_number(prompt: str) -> Optional[float]:
    """Get a positive number from user input."""
    try:
        value = float(input(prompt))
        if value <= 0:
            print("Error: Please enter a positive number")
            return None
        return value
    except ValueError:
        print("Error: Please enter a valid number")
        return None


def main():
    while True:
        print("\nShape Area Calculator")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Square")
        print("5. Exit")
        
        choice = input("\nSelect a shape (1-5): ")
        
        if choice == '5':
            print("Thank you for using the Shape Area Calculator!")
            break
            
        elif choice == '1':
            radius = get_positive_number("Enter radius: ")
            if radius is not None:
                area = circle_area(radius)
                if area is not None:
                    print(f"Area of circle = {area:.2f} square units")
                    
        elif choice == '2':
            length = get_positive_number("Enter length: ")
            if length is not None:
                width = get_positive_number("Enter width: ")
                if width is not None:
                    area = rectangle_area(length, width)
                    if area is not None:
                        print(f"Area of rectangle = {area:.2f} square units")
                        
        elif choice == '3':
            base = get_positive_number("Enter base: ")
            if base is not None:
                height = get_positive_number("Enter height: ")
                if height is not None:
                    area = triangle_area(base, height)
                    if area is not None:
                        print(f"Area of triangle = {area:.2f} square units")
                        
        elif choice == '4':
            side = get_positive_number("Enter side length: ")
            if side is not None:
                area = square_area(side)
                if area is not None:
                    print(f"Area of square = {area:.2f} square units")
                    
        else:
            print("Invalid choice! Please select 1-5")


if __name__ == '__main__':
    main()
