import math
p1= input().split(None, 1)
p2= input().split(None, 1)

x1, y1 = (p1)
x2, y2 = (p2)
s = ((float(x2)-float(x1))**2)+((float(y2)-float(y1))**2)
distance = math.pow(s, 1/2)
print ("DISTANCE: %.4f"%distance)