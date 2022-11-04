'''''
For in em python
interando strings com for
função de rage (start = 0, stop, step 1
'''''

texto = 'Python'
nova_letra = ''

#Pecorre a string e enumera ela
for num,item in enumerate(texto):
    print(num, item, '\n')

#separador
print("_________________")

#mutiplo de 9
for aux in range(0, 91, 9):
    print(aux)

#troca a primeira letra da string texto

for l in texto:
    if l == 'P':
        nova_letra = nova_letra + l.lower()
    else:
         nova_letra += l

print(nova_letra)
