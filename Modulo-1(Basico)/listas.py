"""""
Lista em python
Fatiamento
Append, insert, pop, del, clear, extend, + min, max
"""""
list_name = ['']
list_cpf = ['']
aux = 0
lista = 1

#aumentando o tamanho da lista de acordo com o número de inserções
while aux < lista:
    list_name.append(input('Informe seu nome:'))
    list_cpf.append(input('Informe CPF nome:'))
    aux += 1
    lista += 1
    if list_name[-1] == '':
        list_name.pop()
        list_cpf.pop()
        del(list_name[0])
        del(list_cpf[0])
        break


print(list_name)
print(list_cpf)