i=9
cp = 0
ci = 0
while i > 0:
  i = int(input("Valor?"))
  if i > 0:
    if i % 2 == 0:
      cp= cp + 1
    else:
      ci = ci + 1
pp = cp / (ci+cp) * 100
pi = ci / (ci+cp) * 100      
print("Percentual de Números Pares Digitados %f" %pp)
print("Percentual de Números Ímpares Digitados %f" %pi)