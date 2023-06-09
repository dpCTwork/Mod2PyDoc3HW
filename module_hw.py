
import math
def find_area():
    length = float(input('Please enter the LENGTH of the house: '))
    width = float(input('Please enter the WIDTH of the house: '))
    area = length * width
    print(f"The area of the house is {area} square feet.")

def find_circumf_by_radius():
    radius = float(input('Please enter the RADIUS of the circle: '))
    rad_circumf =  2 * radius * math.pi
    print(f"Circumference by radius (rounded to the nearest 100th): {rad_circumf:.2f}.")

def find_circumf_by_diameter():
    diameter = float(input('Please enter the DIAMETER of the circle: '))
    dia_circumf = diameter * math.pi
    print(f"Circumference by diameter (rounded to the nearest 100th): {dia_circumf:.2f}.")