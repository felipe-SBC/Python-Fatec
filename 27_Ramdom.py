import random
lista1 = [0]*9
i = 0

while i < len(lista1):
    lista1[i]=random.randint(-250,251)
    print(lista1)
    i=i+1
i=0
conta=0
while i<len(lista1):
    if lista1[i]>0:
        conta=conta+1
    i=i+1
print("Quantidade de números positivos %d" %conta)