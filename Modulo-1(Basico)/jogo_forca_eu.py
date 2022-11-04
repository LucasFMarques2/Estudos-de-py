"""""
Jogo da forca, feito de cabeça
"""""
import os

palavra_secreta = input("Informe uma palavra:")
palavra_secreta.lower()
tentativas = len(palavra_secreta)
digitada = []

os.system('cls')

print(f'Você tem {tentativas} tentativas')

while True:
     letra_digitada = input("Informe uma letra:")
     letra_digitada.lower()

     if len(letra_digitada) > 1:
         print("Não pode digitar mais de uma letra")

     digitada.append(letra_digitada)

     if letra_digitada in palavra_secreta:
          print("acertou")
     else:
          print("Errou")
          tentativas -= 1
          print(f"Agora você só tem {tentativas} tentativas")
     secreto_temp = ''
     for letra_digitada in palavra_secreta:
          if letra_digitada in digitada:
               secreto_temp += letra_digitada
          else:
              secreto_temp += '_'
     if secreto_temp == palavra_secreta:
          print("Parabéns você ganhou")
          break
     elif tentativas == 0:
          print("Você perdeu")
          break
     print(secreto_temp)


