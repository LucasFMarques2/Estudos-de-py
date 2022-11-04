""""
Operadores lógicos

and, or, not
in e not in
"""""

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))



if idade >= 18 and idade <= 70:
    print(" é o brad")
if idade > 20 or nome == 'Lucas':
    print(" è o marshoaw")
# Se a idade não for maior qur 20 e nome for diferente de lucas vai executar
if not idade > 20 and nome != "Lucas":
    print("Aobassa")

if 's' in nome:
     print("Tem S aq")
if 'p' not in nome:
     print("Não tem P aq")
