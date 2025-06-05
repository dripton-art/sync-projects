def Area(length, width):
    area = length * width
    return area
    
length = int(input("Enter length: "))
width = int(input("Enter width: "))

print(f"The area of the rectangle is:", Area(length, width))