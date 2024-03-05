import forca
import adivinhacao

def escolha_Jogo():
    print("******************")
    print("**escolha o jogo**")
    print("******************")
    print("(1) Forca, (2) Adivinhação")

    jogo = int(input('escolha uma das opçoes de jogo acima'))
    if escolha == 1:
        forca.jogarForca()
    elif escolha == 2:
        adivinhacao.jogarAdivinha()
    else:
        print("digite 1 ou 2")

if(__name__ == "__main__"):
    escolha_Jogo()