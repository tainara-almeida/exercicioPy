# #Variáveis
# Uma variável é como uma caixa no seu computador com uma etiqueta, ou seja, é um espaço limitado para guardar informações.

# Trazendo este conceito para o cenário do computador, uma variável é um espaço reservado de memória RAM (não se preocupe tanto com o que isso significa) onde dados são armazenados.

# No contexto de Python, o computador identifica esse conjunto de dados por uma palavra, que é o nome da variável. Esse nome deve seguir algumas regras, por exemplo:

# O nome deve começar com uma letra ou underscore "_";
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# E algumas outras regras...

# Atribuição de valor
# A forma mais comum de atribuir valor a uma variável é usando o operador =.

# nome_da_variavel = valor

# No exemplo acima, valor pode ser um número, um texto ou algum outro tipo de variável definida em Python (pode até mesmo ser um tipo que você definiu! Mas isso é uma conversa mais avançada).

# Tipos Básicos de Variáveis
# Texto: str
# Numérico: int, float, complex
# Sequências: list, tuple, range
# Mapas: dict
# Booleana: bool
# E mais algumas não tão importantes no momento...

# Tipos diferentes de variáveis podem interagir quando os devidos cuidados são tomados.

# Em geral, segue-se a regra que, para que duas variáveis de tipos diferentes interajam, tem que haver transformação de uma delas para que se tornem do mesmo tipo.

# A função em Python que mostra qual é o tipo da variável é a função type(nome_da_variavel). A resposta dela é no formato <class 'tipo'>. Por exemplo:

# text = "Hello"

# tipo_text = type(text)

# print(tipo_text) # Espera-se que a saída mostrada no terminal seja <class 'str'>

# Atividade
# No código ao lado, a função print(numero) é usada para escrever o conteúdo da variável numero no terminal.

# Sua missão é:

# no primeiro passo você deve atribuir um tipo int com valor 10 à variável numero;
# no segundo passo você deve atribuir um tipo str com valor 10 à variável numero;
# no terceiro passo você deve atribuir um tipo str com valor Dez à variável numero;

# Lembrando que para atribuir valores do tipo str deve-se utilizar aspas no início e no final do valor

#EXERCICIO 
# Primeiro passo

numero = 10 

print(numero)
# ========================
# Segundo passo

numero = "10"

print(numero)
# ========================
# Terceiro passo
numero = "Dez"

print(numero)

