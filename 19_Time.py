total = int(input())
hours = total//3600
total = total%3600
min = total//60
sec = total%60
print("%i:%i:%i"%(hours,min,sec))