# def procura_caracter (palavra, letra):

#     contador = 0
#     while contador < len(palavra):
#         if palavra[contador] == letra:
#             return True    
#         contador += 1

#     return False

# print(procura_caracter("teste", "s"))
# print(procura_caracter("python eh muito legal", "z")) 
# print(procura_caracter("batatinha roxa", " "))    


#2 Escreva uma função que soma todos os numeros dentro de uma lista

def soma_numeros(lista_de_numeros):

    soma=0
    
    for numeros in lista_de_numeros:
        soma += numeros
    # # print('Isso é a soma da lista {}'.format (soma))
        return soma
       
print(soma_numeros([1,2,3,4]))
print(soma_numeros([0,1,0]))
print(soma_numeros([8,0,7,42,58]))