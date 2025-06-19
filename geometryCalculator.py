# --- Imports ---
import math;


# --- Functions ---

# Area of a rectangle
def areaRectangle(length, width):
    area = round(float(width * length), 2);
    return area;

# Area of a triangle
def areaTriangle(base, height):
    area = round(float(0.5 * (base * height)), 2);
    return area;

def areaCircle(radius):
    area = round(float(math.pi * (radius ** 2)), 2);
    return area;


# --- Main Program ---

# Prompt user for shape
print("\nWelcome to the Shape Area Calculator!");
print("Enter 'R' for Rectangle, 'T' for Triangle, or 'C' for Circle.\n");
shape = input("Your choice: ").strip().lower();


# Prompt user for dimensions & print result
# rectangle
if shape == "r":
    length = float(input("Enter the length: "));
    width = float(input("Enter the width: "));

    result = areaRectangle(length, width);
    print(f"\nThe area of the rectangle is {result} units squared.");
    pass;

# triangle
elif shape == "t":
    base = float(input("Enter the base: "));
    height = float(input("Enter the height: "));

    result = areaTriangle(base, height);
    print(f"\nThe area of the rectangle is {result} units squared.");
    pass;

# circle
elif shape == "c":
    radius = float(input("Enter the radius: "));

    result = areaCircle(radius);
    print(f"\nThe area of the rectangle is {result} units squared.");
    pass;

else:
    print("Invalid shape choice. Please run the program again and choose R, T, or C.");

print("Thank you for using the Shape Area Calculator!\n");