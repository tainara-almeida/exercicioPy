# Números em Python
# Se você fez a tarefa anterior Variáveis e Atribuição de valor lembre-se de que existem três tipos numéricos em Python:

# int
# float
# complex

# Exemplos desses três tipos são:

# x = 1     # int
# y = 3.14  # float
# z = 1j    # complex

# Não se preocupe com o tipo complex, se você se lembra do conjunto dos números complexos, apenas saiba que eles são representados dessa forma em Python, mas na prática não são utilizados a não ser que seu propósito seja algum trabalho científico.

# Recordando, o tipo de uma variável pode ser verificado usando a função type():

# x = 1
# print(type(x))  # O resultado será <class 'int'>

# y = 3.14
# print(type(y))  # O resultado será <class 'float'>

# z = 1j
# print(type(z))  # O resultado será <class 'complex>

# int
# O tipo int representa um número inteiro, ou seja, um número que pertence ao conjunto dos números inteiros, que são os números que "não possuem números depois da vírgula" e podem ser tanto positivos quanto negativos.

# Exemplos:

# x = 1
# y = 270346
# z = -42

# Note que um número inteiro pode ser representado como tendo apenas zeros depois da vírgula como 5.0, mas, para Python (e outras linguagens de programação em geral), quando definimos uma variável dessa forma, ela passa a ser considerada como tipo float.

# float
# O tipo float representa um número real, ou seja, um número que pertence ao conjunto dos números reais, que são os números que possuem números depois da vírgula e também aqueles que não possuem, ou seja, o conjunto dos números inteiros está inteiramente dentro do conjunto dos números reais.

# Exemplos:

# x = 5.0
# y = 3.14
# z = -47.542346


# Conversão de Tipos
# É possível converter entre int e float usando as funções int() e float():

# x = 1
# a = float(x) # Converte o valor de x para float e atribui à variável a

# y = 3.14
# b = int(y)   # Converte o valor de y para int e atribui à variável b

# A conversão de float para int apenas ignora as casas decimais do valor, ou seja, no exemplo acima, a variável b teria como valor o número 3.

# Atividade
# Complete o código ao lado para que, no terminal, sejam impressos os tipos da variável x e da variável y usando a função vista anteriormente.


#===Atividade Números=====
x = 4
y = 26.12

# Tipo da variável x
print(type(x))

# Tipo da variável y
print(type(y))