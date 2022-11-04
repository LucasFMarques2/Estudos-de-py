"""""
Faça um programa que peça ao usário para digitar um número inteiro, informe se este número é par ou impar. 
Caso o usuário não digite um número inteiro, informe que não é um número inteiro
"""""
"""""
Faça um programa que pergunte a hora ao usuário e baseando-se
no horário descrito, exiba a saudação apropriada
"""""
"""""
Faça um programa que peça primeiro o nome do usuári.. Se o nome tiver 4 letras
ou menos escreva "Seu nome é curto", se tiver entre 5 e 6 letras. escreava " Seu nome é normal". mairo que 6
escreava "Seu nome é muito grande"
"""""


#Programa 1

num = input("Informe um número inteiro:");

if num.isdigit():
    if int(num) % 2 == 0:
        print(" Esse numero é par")
    else:
        print("Esse número é impar")
else:
    print("Esse não é um número inteiro")

#Programa 2

hora = input("Informe o horário:")

if hora.isdigit():
    hora = int(hora)

    if hora >=6 and hora < 13:
        print(" Bom dia !")
    elif hora >= 13 and hora < 18:
        print (" Boa tarde")
    elif hora >= 18 and hora < 24:
        print ("Boa noite")
    else:
        print("Boa madrugada")
else:
    print("formato de hora incorreto")

#programa 3

nome = input("Informe seu nome:")

nome = len(nome)

if nome <= 4:
    print("Seu nome é muito curto")
elif nome >= 5 and nome <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito longo")