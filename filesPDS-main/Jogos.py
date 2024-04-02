import forca
import adivinhacao
import jokenpo

def escolJogo():
    print('-------------------------------------------')
    print('-------------Escolha o jogo----------------')
    print('-------------------------------------------')
    print('(1) - Forca')
    print('(2) - Adivinhação')
    print('(3) - Jokenpo')
    escolha = int(input('Digite a opção desejada: '))
    if escolha == 1:
        forca.jogar()
    elif escolha == 2:
        advinhac.jogar()
    elif escolha == 3:
        jokenpo.jogar()
    else:
        print('Digite uma opção certa macaco')

if(__name__=="__main__"):
    escolJogo()