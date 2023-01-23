'''f = open("item.txt", "r")
arquivo = f.read()
print("Arquivo original: ")
print(arquivo)
print("Divisão por linhas: ")
lista = arquivo.split("\n")
print(lista)
print("Divisão de cada linha por espaço em branco")
for linha in lista:
    print(linha.split())'''
 
f = open("item.txt", "r")
arquivo = f.readline()
while arquivo != "":
    print("Linha original")
    print(arquivo)
    arquivo= f.readline()
f.close()