"""""
Formatando valores com modificadores - Aula 5
:s - Texto (string)
:d - Inteiros (int)
:f - Números de ponto flutuante(float)
:.Númerof - quantidade de casas decimais (float)
:caracter(> ou < ou ^)(Quantidade)(tipo - s, d ou f)
> - esquerda
< - Direita
^ - Centro
"""""

num1 = 1

print(f'{num1:0>10}')

nome = input("Informe seu nome:")


print(nome.lower())# tudo minusculo
print(nome.upper())# tudo maiusculo
print(nome.title())# Primeira letra maiuscula
print(f'{nome.title():!^20}')# adicionando 20 caracters e nos espaços vagos acrescentado "!"


