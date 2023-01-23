notas = [0.0]*5
soma = 0.0
i=0
while i<len(notas):
    notas[i] = float(input("Digite a nota do %d  o. aluno: " %  (i+1)))
    soma = soma + notas[i]
    i=i+1
media = soma / len(notas)
print ("A média da turma é %.1f"  %  media)
notas = [0.0]*5
for i in range(len(notas)):
    notas[i] = float(input("Digite a nota do %d o. aluno: " % (i+1)))
print ("Lista de notas: ",notas)
i = 0
while i < len(notas):
    print("nota %do. aluno: %.1d" %(i+1, notas[i]))
    i= i + 1
peca = input()
peca1 = input()
cod1, np1, vu1 = peca.split()
cod2, np2, vu2 = peca1.split()
pagar = (int (np1) * float (vu1)) + (int(np2) * float(vu2))
#como pro split tudo é string, para fazer conta precisa declarar o tipo da var.
print("VALOR A PAGAR: R$ %.2f"%pagar)