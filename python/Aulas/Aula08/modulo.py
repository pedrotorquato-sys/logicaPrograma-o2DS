import os
def soma(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

def limpar_terminal():
    os.system('cls' if os.name =='nt'else'clear')