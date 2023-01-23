def mensagem1():
    print("Ola!")
mensagem1()

def mensagem2(nome):
    print("Olá",nome,"!")

def mensagem3(nome):
    return("Olá",nome)

def Mult(a,b):
    return a*b

def Soma(a,b):
    return(a+b)

def Media(a,b,c):
    return((a+b+c)/3)   

def Conversao(a,b,c,d): 
    a = a + 2**3
    b = b * 2**2
    d = d * 2**1
    c = c * 2**0
    return(a+b+c+d)