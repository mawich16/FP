# Preencha a lista com os números mecanográficos dos autores.
AUTORES = [112903, 119696]

import random

# função do maind display do início do jogo
def abertura():
    print(' ________________________________________________\n|                                                |\n|         *Bem vindo ao Jogo Da Forca!!!*        |\n|________________________________________________|')
    print(' ________________________________________________\n|                                                |\n|    Estás preparado para este grande desafio?   |\n|________________________________________________|')

# função de display da imagem da forca que dependendo do número de erros apresenta o boneco da forca correspondente
def boneco(erros):
    if erros == 0:
       print('\n  _______     ')
       print(' |/      |    ')
       print(' |            ')
       print(' |            ')
       print(' |            ')
       print(' |            ')
       print(' |            ')
       print('_|___         ')
    elif erros == 1:
       print('\n  _______     ')
       print(' |/      |    ')
       print(' |       O    ')
       print(' |            ')
       print(' |            ')
       print(' |            ')
       print(' |            ')
       print('_|___         ')
    elif erros == 2:
       print('\n  _______     ')
       print(' |/      |    ')
       print(' |       O    ')
       print(' |       |    ')
       print(' |            ')
       print(' |            ')
       print(' |            ')
       print('_|___         ')
    elif erros ==3:
       print('\n  _______     ')
       print(' |/      |    ')
       print(' |       O    ')
       print(' |      /|    ')
       print(' |            ')
       print(' |            ')
       print(' |            ')
       print('_|___         ')
    elif erros == 4:
       print('\n  _______     ')
       print(' |/      |    ')
       print(' |       O    ')
       print(' |      /|\   ')
       print(' |            ')
       print(' |            ')
       print(' |            ')
       print('_|___         ')
    elif erros == 5:
       print('\n  _______     ')
       print(' |/      |    ')
       print(' |       O    ')
       print(' |      /|\   ')
       print(' |      /    ')
       print(' |            ')
       print(' |            ')
       print('_|___         ') 
    elif erros == 6:
       print('\n  _______     ')
       print(' |/      |    ')
       print(' |       O    ')
       print(' |      /|\   ')
       print(' |      / \  ')
       print(' |            ')
       print(' |            ')
       print('_|___         ') 

# função de display da imagem quando o jogador perde
def derrota():
    print("          _____       " )
    print("         /     \      " )
    print("        |  _|_  |     " )
    print("        |   |   |     " )
    print("        | R.I.P |     " )
    print("        |       |     " )
    print("        |       |     " )
    print("         \_____/      " )

# função de display da imagem quando o jogador ganha
def vitoria():
    print("        __________     ")
    print("       (__________)    ")
    print("      .-\        /-.   ")
    print("     | (|        |) |  ")
    print("      '-|        |-'   ")
    print("        \        /     ")
    print("         ':    :'      ")
    print("           )  (        ")
    print("         _.'  '._      ")
    print("        '--------'     ")

# função que simplifica a palavra para facilitar a comparação de strings, a palavra em questão passa a ser constituida por letras maiusculas e os caracteres especiais são substituidos pela sua forma simplificada
def standard(word):
    word = word.upper()
    word = word.replace('À', 'A').replace('Á', 'A').replace('Ã', 'A').replace('É', 'E').replace('È', 'E').replace('Ê', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Õ', 'O').replace('Ú', 'U').replace('Ç', 'C')
    return word

# função que, se tentativa estiver cetra, substitui essa letra no local cert, sendo as restantes letras apresentadas como '_'
def traços_palavra(traços, secret_standard, tentativa_standard, secret):
    for i in range(len(traços)):
        if tentativa_standard == secret_standard[i]:
            traços[i] = secret[i]
    return traços

# função que regista o número de jogos e de vitórias e no fim do jogo, caso tenha sido uma vitória, dá display a esses valores
def win_streak():
    global numero_vitorias
    global numero_jogos
    numero_vitorias += 1
    numero_jogos += 1
    print('Número de vitórias: ', numero_vitorias, end=' ')
    print('Número de jogos: ', numero_jogos)
    return numero_vitorias, numero_jogos

# função que regista o número de jogos e de vitorias e no fim do jogo, caso tenha sido uma derrota, dá display a esses valores
def lose_streak():
    global numero_vitorias
    global numero_jogos
    numero_jogos += 1
    print('Número de vitórias: ', numero_vitorias, end=' ')
    print('Número de jogos: ', numero_jogos)
    return numero_vitorias, numero_jogos

# função que permite ao utilizador jogar novamente ou não sem ter de correr o código novamente
def repetir_jogo():
    repetir=input('Queres jogar outra vez? (Sim/Nao) ')
    repetir_standard=standard(repetir)
    if repetir_standard=='SIM':
        main()
    elif repetir_standard=='NAO':
        print('Obrigado por jogares, até à próxima!')
    else:
        print('Resposta inválida, tenta outra vez')
        repetir_jogo()

# função de tentativas de adivinhar a palavra sercreta, string 'secret', escolhida aleatoriamente na função main()
def palavra(secret):
    secret=str(secret)     # converte o parametro 'secret' para string para o maior facilidade e manuseamento
    erros = 0
    letras_erradas = []    # lista que vai guardar as tentativas de letras erradas do utilizador
    letras_certas = []     # lista que vai guardar as tentativas de letras corretas do utilizador
    palavras_erradas = []  # lista que vai guardar as tentativas de palavras erradas do utilizador
    palavras_certas = []   # lista que vai guardar as tentativas de palavras corretas do utilizador
    espaços = len(secret)
    secret_standard=standard(secret)  # conversão da string 'secret' para parametros standard para uma maior facilidade de comparação
    secret2=set(secret_standard)      # 'secret2' é o conjunto de letras constituido pelas letras de 'secret_standard' mas sem repetição para poder ser comparado com a lista letras_certas que também não tem repetições 
    traços = ['_'] * espaços          # criação da lista com o número de '_' igual ao número de letras na palavra 'secret'  para depois substituir aqui as letras adivinhadas corretas nas respetivas posições



    while erros < 6:

        tentativa = input("Escolhe uma letra/palavra: ")

        while tentativa.isalpha()==False:  # verificar se o input é uma letra, pois caso seja um número ou qualquer outro caracter não pode contar como uma tentativa do jogo
            print('Caracter não válido, tente novamente ')
            tentativa=input("Escolhe uma letra/palavra: ")
        
        tentativa_standard=standard(tentativa)  # conversão da string 'tentativa' para parametros standard para uma maior facilidade de comparação

        if len(tentativa) == 1:
            if tentativa_standard in letras_erradas or tentativa_standard in letras_certas:
                print("Letra já tentada")
            elif tentativa_standard in secret_standard:
                    boneco(erros)
                    print("Letra certa :)")
                    letras_certas.append(tentativa_standard)
                    print('Letras erradas: ' + ', '.join( letras_erradas))
            else:
                erros += 1
                boneco(erros)
                print("Letra errada :(")
                letras_erradas.append(tentativa_standard)
                print('Letras erradas: ' + ', '.join( letras_erradas))
                print('Tens mais {} tentativas'.format(6-erros))
            if sorted(secret2)==sorted(letras_certas):
                print('Parabéns, ganhaste o jogo, conseguiste acertar na palavra secreta', end=' ')
                print(secret)
                vitoria()
                win_streak()
                repetir_jogo()
                break

            traços=traços_palavra(traços,secret_standard,tentativa_standard,secret)

            for i in range(len(traços)):
                print(traços[i], end=' ')

        elif len(tentativa) == espaços:
            if tentativa_standard in palavras_erradas or tentativa_standard in palavras_certas:
                print("Palavra já tentada")
            elif tentativa_standard == secret_standard:
                print('Parabéns, ganhaste o jogo, conseguiste acertar na palavra secreta:', end=' ')
                print(secret)
                vitoria()
                win_streak()
                repetir_jogo()
                break
            else:
                print('Palavra errada:(')
                palavras_erradas.append(tentativa_standard)
                erros += 1
                boneco(erros)
                print('Palavras erradas: ' + ', '.join( palavras_erradas))
                print('Tens mais {} tentativas'.format(6-erros))
        else:
            print('Escreva apenas uma letra ou uma palavra com o mesmo número de letras que a palavra secreta')
    if erros == 6: 
        print('Perdeste o jogo, a palavra secreta era' , end=' ')
        print(secret)
        derrota()
        lose_streak()
        repetir_jogo()

# função do jogo
def main():
    from wordlist import words1, words2
    
    words = words1 + words2    # palavras de ambos os tipos

    import sys                  # INCLUA estas 3 linhas para permitir
    if len(sys.argv) > 1:       # correr o programa com palavras dadas:
         words = sys.argv[1:]    #   python3 forca.py duas palavras

    # Escolhe palavra aleatoriamente
    secret = random.choice(words).upper()

    #inicia o jogo
    abertura()
    palavra(secret)


if __name__ == "__main__":
    numero_vitorias = 0
    numero_jogos = 0
    main()




