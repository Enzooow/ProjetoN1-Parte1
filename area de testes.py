numero_sala = 1
linha1 = "Você está na sala:"
interação = 1


print("{} {}" .format(linha1, numero_sala))
print("Escolha seu caminho:")
print("[1] - Caminho vermelho")
print("[2] - Caminho preto")
caminho = int(input())
interação += 1

while interação < 7:

    if (numero_sala == 8 and caminho == 1) or (numero_sala == 7 and caminho == 2):
        print("Sua guilda avista uma luz no final do tunel... É a saída!!! Vocês correm em direção a ela e saem.")
        print("W W W   III    N   N")
        print("W W W    I     NN  N")
        print("W W W    I     N N N")
        print(" WWW     I     N  NN")
        print(" W W    III    N   N")

        break

    if numero_sala == 8 and caminho == 2:
        import random
        novo_numero = random.randint(1, 5)
        print("{} {}" .format(linha1, novo_numero))
        print("Escolha seu caminho:")
        print("[1] - Caminho vermelho")
        print("[2] - Caminho preto")
        caminho = int(input())
        interação += 1

        numero_sala = novo_numero

        if caminho == 1:
            numero_sala += 1
            print("{} {}" .format(linha1, numero_sala))
            print("Escolha seu caminho:")
            print("[1] - Caminho vermelho")
            print("[2] - Caminho preto")
            caminho = int(input())
            interação += 1

        elif caminho == 2:
            numero_sala += 2
            print("{} {}" .format(linha1, numero_sala))
            print("Escolha seu caminho:")
            print("[1] - Caminho vermelho")
            print("[2] - Caminho preto")
            caminho = int(input())
            interação += 1

    if numero_sala == 5 and caminho == 1:
        numero_sala += 1
        print("{} {}" .format(linha1, numero_sala))
        print("Escolha seu caminho:")
        print("[1] - Caminho vermelho")
        caminho = int(input())
        interação += 1

    if numero_sala == 4 and caminho == 2:
        numero_sala += 2
        print("{} {}" .format(linha1, numero_sala))
        print("Escolha seu caminho:")
        print("[1] - Caminho vermelho")
        caminho = int(input())
        interação += 1

    if caminho == 1:
        numero_sala += 1
        print("{} {}" .format(linha1, numero_sala))
        print("Escolha seu caminho:")
        print("[1] - Caminho vermelho")
        print("[2] - Caminho preto")
        caminho = int(input())
        interação += 1

    elif caminho == 2:
        numero_sala += 2
        print("{} {}" .format(linha1, numero_sala))
        print("Escolha seu caminho:")
        print("[1] - Caminho vermelho")
        print("[2] - Caminho preto")
        caminho = int(input())
        interação += 1

else:
    print("Você e sua guilda se perderam na dungeon e acabaram morrendo pelas criaturas místicas que viviam nela!")
    print("GGGGG   AAA   M   M  EEEEE      OOO   V   V  EEEEE  RRRR")
    print("G      A   A  MM MM  E         O   O  V   V  E      R   R")
    print("G GGG  AAAAA  M M M  EEEEE     O   O   V V   EEEEE  RRRR")
    print("G   G  A   A  M   M  E         O   O   V V   E      R  R")
    print("GGGGG  A   A  M   M  EEEEE      OOO     V    EEEEE  R   R")
