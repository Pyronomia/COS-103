import math
temperature = float(input("Enter your desired temperature: "))
unit = input("Celsius or Fahrenheit (C or F?): ")

if unit == "C":
    temperature = (temperature * 1.8) + 32
    unit = "F"
    print("Your new temperature is:",temperature,unit)
elif unit == "F":
    temperature = (temperature - 32)/1.8
    unit = 'C'
    print(f"Your new temperature is: {temperature}{unit}")
else: 
    print("Invalid unit")

name = "Sinmi"
age =  18
print(type(name))
print(type(age))

shape = input("Circle, Triangle or Rectangle(C, T or R): ")
if shape == "C":
    radius = float(input("Enter radius: "))
    area = math.pi * radius**2
    print(f"The area of the circle is: {area}")
elif shape == "T":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")
elif shape == "R":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area}")
else: 
    print("Invalid Shape")
