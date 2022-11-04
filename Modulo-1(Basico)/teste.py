#Login de usuário

login_erro = True

login = input("Login:")
senha = input("Senha:")
login = login.title()

while login_erro:
    login_correto = 'Lust'
    senha_correta = 'lucas'

    if login_correto != login or senha_correta != senha:
        print("Login ou senha inválida\n")
        print("Tente novamente")

        login = input('Login:')
        senha = input('Senha:')
        continue
    else:
        print(f'Bem-vindo {login}')
        login_erro = False

