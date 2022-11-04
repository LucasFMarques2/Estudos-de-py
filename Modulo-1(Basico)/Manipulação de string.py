"""""
Manipulando Strings - Aula 6
* String indices
* Fatiamento de Strings [Inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo

links:
https://docs.python.org/3/library/stdtypes.html (tipos de built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
"""""

#positivos  [012345678]
texto  =    'Python s2'
#Negativos -[987654321]

url = 'www.youtube.com/Xpsoq10s/passowrds' #retira as ultimas 9 letras
print(url[:-9])

nova_string = texto[2:6] #fatiar uma string
print(nova_string)

nova_nova_string = texto[0::2]#Pulando o caracter de 2 em 2
print(nova_nova_string)
