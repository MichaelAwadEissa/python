def area():
    choice = input('Enter your shape ("c" for circle, "s" for square, "t" for triangle, "r" for rectangle): ').lower()

    if choice == "c":
        num1 = float(input("Enter the radius of the circle: "))
        area = 3.14 * (num1 ** 2)
    elif choice == "s":
        num1 = float(input("Enter the length of the square: "))
        area = num1 ** 2
    elif choice == "t":
        num1 = float(input("Enter the base length of the triangle: "))
        num2 = float(input("Enter the height of the triangle: "))
        area = 0.5 * num1 * num2
    elif choice == "r":
        num1 = float(input("Enter the length of the rectangle: "))
        num2 = float(input("Enter the width of the rectangle: "))
        area = num1 * num2
    else:
        return "Invalid shape choice."

    return area

print(f"area:{area()}")
