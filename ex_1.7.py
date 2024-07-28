import math

def calc_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

try:
    a1 = float(input("Enter side a1: "))
    b1 = float(input("Enter side b1: "))
    c1 = float(input("Enter side c1: "))
    a2 = float(input("Enter side a2: "))
    b2 = float(input("Enter side b2: "))
    c2 = float(input("Enter side c2: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    
    
area1 = calc_area(a1, b1, c1)
area2 = calc_area(a2, b2, c2)
total_area = area1 + area2
    
cont_1 = (area1 / total_area) * 100
cont_2 = (area2 / total_area) * 100
    
print(f"Area of the first triangle: {area1:.2f}")
print(f"Area of the second triangle: {area2:.2f}")
print(f"Total area enclosed by both triangles: {total_area:.2f}")
print(f"First triangle's contribution: {cont_1:.2f}%")
print(f"Second triangle's contribution: {cont_2:.2f}%")

