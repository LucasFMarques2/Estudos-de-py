# indice

frase = 'raridade é a rainha roer um rato em cima do rei de roma'
tamanho_frase = len(frase)
cont = 0
nova_str = ''

while cont < tamanho_frase:
    letra = frase[cont]
    if letra == 'r':
       nova_str += 'R'
    else:
       nova_str += letra
    cont += 1

print(nova_str)