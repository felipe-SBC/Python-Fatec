value = int(input())
print(value)
cem = value//100
value=value%100
cinq = value//50
value=value%50
vint = value//20
value=value%20
dez = value//10
value=value%10
cin = value//5
value=value%5
dois = value//2
value=value%2
um = value/1
print("%i note(s) of $ 100,00"%cem)
print("%i note(s) of $ 50,00"%cinq)
print("%i note(s) of $ 20,00"%vint)
print("%i note(s) of $ 10,00"%dez)
print("%i note(s) of $ 5,00"%cin)
print("%i note(s) of $ 2,00"%dois)
print("%i note(s) of $ 1,00"%um)