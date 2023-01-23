value = float(input())
print(value)
hundred = value//100
value=value%100
fifty = value//50
value=value%50
twenty = value//20
value=value%20
ten = value//10
value=value%10
five = value//5
value=value%5
two = value//2
value=value%2
one = value//1
value = value%1
fiftyCent = value//0.5
value=value%0.5
twentyCent= value//0.25
value=value%0.25
tenCent= value//0.10
value=value%0.10
fiveCent = value//0.05
value=value%0.05
oneCent = value/0.01
print("NOTES:")
print("%i note(s) $ 100.00"%hundred)
print("%i note(s) $ 50.00"%fifty)
print("%i note(s) $ 20.00"%twenty)
print("%i note(s) $ 10.00"%ten)
print("%i note(s) $ 5.00"%five)
print("%i note(s) $ 2.00"%two)
print("CENTS:")
print("%i cent(s) $ 1.00"%one)
print("%i cent(s) $ 0.50"%fiftyCent)
print("%i cent(s) $ 0.25"%twentyCent)
print("%i cent(s) $ 0.10"%tenCent)
print("%i cent(s) $ 0.05"%fiveCent)
print("%i cent(s) $ 0.01"%oneCent)