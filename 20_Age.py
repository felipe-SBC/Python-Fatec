age = int(input())
years = age//365
age = age%365
months = age//30
days = age%30
print("%i ano(s)"%years)
print("%i mes(es)"%months)
print("%i dia(s)"%days)