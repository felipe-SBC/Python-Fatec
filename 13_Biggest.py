vect= input().split(None, 2)
number1 = int(vect[0])
number2= int(vect[1])
number3= int(vect[2])
m = (number1 + number2 + abs(number1-number2))/2
s = (number3 + m + abs(number3 - m))/2
print("%i it's the biggest"%s)