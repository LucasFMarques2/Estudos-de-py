"""""
*Criar variáveis para nome (str), idade (int)
*Altura (float) e peso (Float) de uma pessoa
*Criar variável com o ano atual (int)
*Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
*obter o IMC da pessoa cm 2 casas decimais (pesoa e na altura da pessoa)
*Exibir um texto com todos os valores na tela usando o F-String ( com as chaves)
"""""

nome = "Lucas"
idade = 23
altura = 1.60
peso = 67.23
ano = 2022


print(f'{nome} tem {idade} anos, {altura} de altura, pesa {peso}, nasceu em {ano - idade} e o IMC é:{peso / altura ** 2:.2f}')

print('"ja sei!"')