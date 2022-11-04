# Entrada de dados pessoais
"""""
nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")
dada_nasc = 2022 - int(idade)
print()

print("*DADOS PESSOAIS*")
print("Nome:", nome)
print("Idade:", idade)
print("Nascimento:", dada_nasc)
"""""

#calculadora



retorno = 's'

while retorno == 's':
    num1 = int(input("Informe um numero: "))
    char = input("Informe a operação: ")
    num2 = int(input("Informe um numero: "))


    if char == '+':
        print('Total: ', num1 + num2)
    elif char == '-':
        print('Total: ', num1 - num2)
    elif char == '*':
        print('Total: ', num1 * num2)
    elif char == '**':
        print('Total: ', num1 ** num2)
    elif char == '/':
        print('Total: ', num1 / num2)
    else:
         print("Operação inválido")
    retorno = input("Deseja fazer novo calculo?(S/N)")



