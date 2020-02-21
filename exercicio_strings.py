#Strings

# Uma string é um tipo de dado usado para representar texto. Em Python, strings são definidas usando aspas simples ou duplas, como no exemplo abaixo

# x = 'hello'

# y = "world"

# É possível ainda definir strings que ocupam varias linhas usando três aspas simples ou duplas na abertura e no fechamento, por exemplo:

# a = '''Primeira linha
# segunda linha
# terceira linha'''

# b = """Primeira linha
# segunda linha
# terceira linha"""

# Acessando Caractéres Específicos
# Strings são considerados vetores em diversas linguagens, e, em Python, isso não é diferente. Isso significa que o conteúdo de uma string é na verdade uma coleção de caractéres, cada um representado por uma posição específica.

# Cada posição pode ser acessada indicando um índice, ou seja, um número que representa a posição daquele caractér, começando da posição 0, por exemplo:

# x = 'hello'
#    # 01234 <- posições

# print(x[0])   # Deve retornar apenas a letra 'h'

# print(x[2])   # Deve retornar apenas a letra 'l'

# Pode-se também especificar pedaços de uma string usando a notação de intervalo de posições [inicio:fim]:

# x = 'helloWorld'
#    # 0123456789

# print(x[3:7]) # Deve retornar apenas o pedaço referente aos indices 3, 4, 5 e 6 (o índice
#               # do fim é sempre excluido), ou seja, deve retornar apenas 'loWo'

# Length
# Para obter o tamanho de uma string, ou seja, quantos caractéres ela possui, deve-se utilizar a função len(). 

# x = 'hello'

# tamanho = len(x)

# print(tamanho) # Deve retornar 5, ou seja, len retorna um tipo int

# Métodos de Strings

# Não falamos sobre métodos e nem funções ainda, mas entenda-os, por enquanto, como palavras especiais que executam várias instruções de uma vez, ou seja, são blocos de código agrupados por uma palavra especial.

# Métodos também são funções, mas são definidas em contextos específicos e servem apenas nesses contextos. Por exemplo, existem funções que funcionam apenas com strings, então conevenciona-se chamar essas funções de métodos, porque são especialmente feitas para funcionarem com strings.

# strip()
# O método strip() remove espaços do início e do final de uma string, por exemplo:

# x = '   hello world       '

# x_strip = x.strip()

# print(x_strip)      # Deve retornar apenas 'hello world' sem os espaços

# lower() e upper()
# O método lower() retorna a string com todas as letras minúsculas, ou seja, qualquer letra maiúscula é transformada em minúscula.

# Da mesma forma, o método upper() transforma todas as letras em maiúsculas:

# x = 'HeLLo WoRld'

# x_lower = x.lower()

# x_upper = x.upper()

# print(x_lower)      # Deve retornar 'hello world'

# print(x_upper)      # Deve retornar 'HELLO WORLD'

# replace() 
# O método replace() é utilizado para substituir qualquer pedaço de uma string por outra string:

# x = 'Hello World'

# x_replace = x.replace('World', 'Universe')

# print(x_replace)     # Deve retornar 'Hello Universe'

# split() 
# O método split() é usado para separar a string em pedaços de acordo com separador especificado, por exemplo:

# x = 'Hello, World'

# x_split = x.split(',') # Usando a vírgula como separador

# print(x_split)         # Deve retornar ['Hello', ' World'] que é uma lista com as duas strings
#                        # separadas (veremos listas nas próximas aulas)

# Existem diversos outros métodos de strings, esses foram apenas alguns dos mais utilizados. Uma lista de todos os métodos pode ser vista na referência https://www.w3schools.com/python/python_ref_string.asp

# Concatenação
# A operação de concatenação é o que permite juntar duas ou mais strings. Isso é feito utilizando a operação de soma +:

# a = 'hello'
# b = 'world'

# print(a + ' ' + b)  # Deve retornar 'hello world'

# format() 
# Como foi visto na seção sobre variáveis, não podemos combinar números e strings apenas usando o operador de concatenação, pois essa operação é considerada uma interação entre um número e uma string.

# Porém, usando o método format() é possível introduzir números dentro de string, pois este método foi programado para transformar o número num tipo str e depois concatenar com a string original:

# idade = 26

# # texto = 'Tenho' + idade + ' anos' ---> Isso resultaria num erro

# texto = 'Tenho {} anos'

# print(texto.format(idade))  # Deve retornar 'Tenho 26 anos'

# Nesse caso, reservamos um local especial na string para introduzir a variável idade usando as chaves {}.

# Esse método não é exclusivo para introduzir números, pode-se utilizá-lo para incluir outras strings no local em que as chaves {} foram colocadas.

# Caractér de Escape
# Às vezes é necessário incluir caractéres dentro de uma string, como, por exemplo, incluir aspas simples ou duplas no conteúdo do texto e não início e final da definição, ou então especificar uma quebra de linha (um "enter" para pular de linha).

# Nesses casos, utiliza-se o caractér \ chamado de "contra-barra". Por exemplo:

# a = "Aspas duplas \" dentro da string"

# print(a) # Deve retornar Aspas duplas " dentro da string

# b = "Quebra de\nlinha" # \n é lido como um "enter" para pular uma linha

# print(b) # Deve retornar
# # Quebra de
# # linha

# Atividade
# Execute as tarefas especificadas nos comentários no código ao lado usando os métodos e operações que você viu nesta seção.

texto = 'Aprender Python eh muito legal'

# Use uma função para imprimir o número de caractéres da variável texto
tamanho = len(texto)

print(tamanho)


# Imprima a variável texto com todas as letras em minúsculas
texto_lower = texto.lower()

print(texto_lower)


# Imprima a variável texto concatenada com a variável complemento
complemento = '\nYaaaaay!'

print(texto + complemento)


# Imprima a variável texto trocando a palavra 'legal' por 'bacana'
texto_replace = texto.replace("legal", "bacana")

print(texto_replace)


