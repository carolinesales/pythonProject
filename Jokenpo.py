import random

vitoria1 = 0
vitoria2 = 0
continua = 1
print("_----------------------------------------------------------------------------------------------------------------")
print("|                                      Bem vindo(a) ao Jokenpô!                                                 |")
print("_________________________________________________________________________________________________________________")
print("| Primeiramente vamos as regras do jogo.                                                                        |\n"
      "| Inicialmente escolha entre pedra/papel/tesoura                                                                |")
print("| a tesoura corta o papel, mas quebra com a pedra; o papel embrulha a pedra, mas é cortada pela tesoura e a     |\n"
      "| pedra quebra a tesoura e é embrulhada pelo papel.                                                             |")
print("-----------------------------------------------------------------------------------------------------------------")
opcao = int(input("Escolha a modalidade do jogo.\n1- Pessoa x Pessoa\n2- Pessoa x Computador\n3- Computador x Computador"))
if opcao == 1:
    while continua == 1:
        pessoa1 = int(input("1- Pedra\n2- Papel\n3- Tesoura"))
        pessoa2 = int(input("1- Pedra\n2- Papel\n3- Tesoura"))
        if pessoa1 == pessoa2:
            print("Empate")

        elif pessoa1 == 1 and pessoa2 == 2: #--------------------------- PEDRA - PAPEL
            print("Vitória do segundo jogador")
            vitoria2 = vitoria2 + 1
        elif pessoa1 == 2 and pessoa2 == 3: # -------------------------- PAPEL - TESOURA
            print("Vitória do segundo jogador")
        elif pessoa1 == 3 and pessoa2 == 1: #--------------------------- TESOURA - PEDRA
            print("Vitória do segundo Jogador")
            vitoria2 = vitoria2 + 1


        elif pessoa2 == 1 and pessoa1 == 2: # -------------------------- PEDRA - PAPEL
            print("Vitória do primeiro jogador")
            vitoria1 = vitoria1 + 1
        elif pessoa2 == 2 and pessoa1 == 3: # -------------------------- PAPEL - TESOURA
            print("Vitória do primeiro jogador")
            vitoria1 = vitoria1 + 1
        elif pessoa1 == 1 and pessoa2 == 3:# --------------------------- PEDRA - TESOURA
            print("Vitória do primeiro jogador")
            vitoria1 = vitoria1 + 1

        continua = int(input("Deseja continuar a jogar?\n1- sim\n2- não"))

elif opcao == 2:
    while continua == 1:
        pessoa1 = int(input("1- Pedra\n2- Papel\n3- Tesoura"))
        pessoa2 = random.randint(1,3)
        if pessoa1 == pessoa2:
            print("Empate")
        elif pessoa1 == 1 and pessoa2 == 2:
            print("Vitória do segundo jogador")
            vitoria2 = vitoria2 + 1
        elif pessoa1 == 2 and pessoa2 == 3:
            print("Vitória do segundo jogador")
            vitoria2 = vitoria2 + 1
        elif pessoa2 == 1 and pessoa1 == 2:
            print("Vitória do primeiro jogador")
            vitoria1 = vitoria1 + 1
        elif pessoa2 == 2 and pessoa1 == 3:
            print("Vitória do primeiro jogador")
            vitoria1 = vitoria1 + 1
        elif pessoa1 == 1 and pessoa2 == 3:
            print("Vitória do primeiro jogador")
            vitoria1 = vitoria1 + 1
        elif pessoa2 == 1 and pessoa1 == 3:
            print("Vitória do segundo jogador")
            vitoria2 = vitoria2
        continua = int(input("Deseja continuar a jogar?\n1- sim\n2- não"))


elif opcao == 3:
    while continua == 1:

        pessoa1 = random.randint(1,3)
        pessoa2 = random.randint(1, 3)
        if pessoa1 == pessoa2:
            print("Empate")
        elif pessoa1 == 1 and pessoa2 == 2:
            print("Vitória do segundo jogador")
            vitoria2 = vitoria2 + 1

        elif pessoa1 == 2 and pessoa2 == 3:
            print("Vitória do segundo jogador")
            vitoria2 = vitoria2 + 1
        elif pessoa2 == 1 and pessoa1 == 2:
            print("Vitória do primeiro jogador")
            vitoria1 = vitoria1 + 1
        elif pessoa2 == 2 and pessoa1 == 3:
            print("Vitória do primeiro jogador")
            vitoria1 = vitoria1 + 1
        elif pessoa1 == 1 and pessoa2 == 3:
            print("Vitória do primeiro jogador")
            vitoria1 = vitoria1 + 1
        elif pessoa2 == 1 and pessoa1 == 3:
            print("Vitória do segundo jogador")
            vitoria2 = vitoria2
        continua = int(input("Deseja continuar a jogar?\n1- sim\n2- não"))

print("Primeiro jogador ganhou",vitoria1, "vezes\n Segundo jogador ganhou",vitoria2,"vezes\n")

print("Alunos: Caroline Videira Sales"
      "        Natan Batalha de Araújo"
      "        Nicolas Lamback de Paulo"
      "        Stuart Henrique Correa Pereira")