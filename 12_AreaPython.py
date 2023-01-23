vect = input().split(None, 2)
a = float(vect[0])
b = float(vect[1])
c = float(vect[2])
triangle = (a*c)/2
circle = c**2 * 3.14159
trapezio =((a+b)*c)/2
square = b * b
rectangle = a * b
print("TRIANGLE: %.3f"%triangle)
print("CIRCLE: %.3f"%circle)
print("TRAPEZIO: %.3f"%trapezio)
print("SQUARE: %.3f"%square)
print("RECTANGLE: %.3f"%rectangle)