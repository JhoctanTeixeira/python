def computador_escolhe_jogada(n, m):
    quantia = n % (m + 1)
    if quantia > 0:
        print ("Computador retirou", quantia, "peças")
    return quantia

def usuario_escolhe_jogada(n, m):
    jogada = 0
    contador = 0
    while jogada == 0:
        while (contador == 0):
            jogada = int(input("Quantas peças você vai tirar? "))
            if (jogada > m):
                print("Oops! Jogada inválida! Tente de novo.\n")
                jogada == 0
            else:
                contador = contador + 1
    return jogada

def partida():
    contador_rodadas = 0
    pc_vencedor = 0
    user_vencedor = 0
    while contador_rodadas < x :
        contador = 1
        while contador == 1:
            n = int(input("Quantas peças? "))
            m = int(input("Limite de peças por jogada? "))
            if m > n:
                print("\nOops! Jogada inválida! Tente de novo.")
                contador == 1
            else:
                contador = contador + 1
        
        Validador_de_jogada = True
        if n % (m + 1 ) == 0: 
            print("\nVocê começa!\n")
            Validador_de_jogada = True
            jogada = usuario_escolhe_jogada(n, m)
            n = n - jogada
            print("Agora restam", n ,"peças no tabuleiro.\n")
        else:
            print("\nComputador começa!\n")
            Validador_de_jogada = False
            jogada = computador_escolhe_jogada(n, m)
            n = n - jogada
            print("Agora restam", n ,"peças no tabuleiro.\n")
                    
        while n != 0:
            if(Validador_de_jogada == True):
                jogada = computador_escolhe_jogada(n, m)
                Validador_de_jogada = False
                n = n - jogada
                print("\nAgora restam", n ,"peças no tabuleiro.\n")
                if (n == 0):
                    print("Computador venceu!")
                    pc_vencedor = pc_vencedor + 1
                    contador_rodadas = contador_rodadas + 1
                    if (x == 1):
                        break
                    elif (contador_rodadas < 3):
                        print("\n**** Rodada", contador_rodadas + 1,"****\n")
                    else:
                        print("**** Final do campeonato! ****")
                        print("Placar: Você",user_vencedor ,"X", pc_vencedor,"Computador")
            else:
                jogada = usuario_escolhe_jogada(n, m)
                n = n - jogada
                print("Agora restam", n ,"peças no tabuleiro.\n")
                Validador_de_jogada = True
                if (n == 0):
                    print("Parabéns, você ganhou!")
                    
                    user_vencedor = user_vencedor + 1
                    contador_rodadas = contador_rodadas + 1
                    if (contador_rodadas < 3):
                        print("\n**** Rodada",  contador_rodadas + 1,"****\n")
                    else:
                        print("**** Final do campeonato! ****")
                        print("Placar: Você",user_vencedor ,"X", pc_vencedor,"Computador")
                    
print("Bem-vindo ao jogo do NIM! Escolha:\n")
x = int (input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))

if (x == 1):
    print("\nVocê escolheu uma partida isolada\n")
    x = 1
    partida()
else:
    print("\nVoce escolheu um campeonato!\n")
    print("**** Rodada 1 ****\n")
    x = 3
    partida()