"""""
While em python - Aula 7
utilizando para realizar acções enquanto
uma condição for verdadeira
"""""

nome = input("Login:")
senha = input("Senha:")

nome = nome.title()

login_correto = 'Lust'
senha_correta = 'Protu22!'

if nome == login_correto and senha == login_correto:
    print(f'Bem vindo {nome}')

else:

    while senha != senha_correta or login_correto != nome:
        print("Login ou senha inválido!\n")
        print("Tente novamente\n")
        nome = input("Login:")
        senha = input("Senha:")
        nome = nome.title()
    else:
        print(f'Bem vindo {nome}')

num = 0
