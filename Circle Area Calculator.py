def calculate_area_of_circle(radius):
    pi = 3.14
    area = pi * radius ** 2
    return area

while True:
    radius_input = input("Please enter the radius of the circle (or enter 'Q' to quit):")

    if radius_input.lower() == 'q':
            print("Thank you for using the circle area calculator. Goodbye!")
            break

    try:
        radius = float(radius_input)
        if radius <=0:
            print("Radius must be a positive number.")
        else:
                area = calculate_area_of_circle(radius)
                print("The area of the circle is", area)
    except ValueError:
            print("Invalid input. Please enter a valid number or 'Q' to quit.")
