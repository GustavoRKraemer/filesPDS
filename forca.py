
palavra_secreta = "botafogo"
letras_acertadas = ["_","_","_","_","_","_","_","_"]
tentativas = 10
def jogarForca():

while tentativas > 0 and "_" in letras_acertadas:
    palpite = input("Digite uma letra:").lower()
    
    if palpite in palavra_secreta: 
        index = 0
        for letra in palavra_secreta:
            if palpite == letra: 
                letras_acertadas[index] = letra
            index += 1
    else: 
        tentativas -= 1
        print(f"Você tem {tentativas} restantes.")
        
    print(" ".join(letras_acertadas))
        
if "_" not in letras_acertadas:
    print ("Parabéns você ganhou!")
else: 
    print (f"Que pena, você perdeu a palavra era: {palavra_secreta}.")

if(__name__ == "__main__"):
    jogarForca()