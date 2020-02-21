#1 Escreva uma função para encontrar o máximo de três números

def maximo_de_tres(n1,n2,n3):

    if n1> n2 and n1> n3:   
        return n1
    elif n2> n3 and n2> n1: 
        return n2  
    else:
        return n3

print(maximo_de_tres(7,4,9))
print(maximo_de_tres(3,81,27))
print(maximo_de_tres(0,1,0))

#2 Escreva uma função que soma todos os numeros dentro de uma lista

def soma_numeros(lista_de_numeros):

    soma=0
    
    for numero in lista_de_numeros:
        soma += numero
    return soma
       
print(soma_numeros([1,1,1]))
print(soma_numeros([8,0,7,42,58]))

# 3 Escreva uma função que procura um caractér numa string


def procura_caracter (palavra, letra):

    contador = 0
    while contador < len(palavra):
        if palavra[contador] == letra:
            return True    
        contador += 1

    return False

print(procura_caracter("teste", "s"))
print(procura_caracter("python eh muito legal", "z")) 
print(procura_caracter("batatinha roxa", " "))    

#Exercicios extras:
def contar_caracter (palavra,letras):

    conta = 0
    contador = 0
    while contador < len(palavra):
        if palavra[contador] == letras:
            conta += 1
    
        contador +=1
    return conta
print(contar_caracter("tainara","a"))


def soma_tudo (n1,n2,n3):

    contador = 0
    soma_y =0

    while contador < 2:]
        soma_x = (n1 + n2) /n3
        contador += 1
        soma_y += soma_x 

    return soma_y 
    
      
print(soma_tudo(10,20,30))
