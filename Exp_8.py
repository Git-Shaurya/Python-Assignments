import math

def calculate_area(shape, a, b=0):
    if shape == "circle":
        return math.pi * a * a
    elif shape == "rectangle":
        return a * b
    elif shape == "triangle":
        return 0.5 * a * b

print("Area of circle:", calculate_area("circle", 5))
print("Area of rectangle:", calculate_area("rectangle", 4, 6))
print("Area of triangle:", calculate_area("triangle", 4, 6))