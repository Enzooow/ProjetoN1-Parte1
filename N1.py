def salas(numero_sala):
    print("Você está na sala: " + numero_sala)
    print("Escolha seu caminho:")
    print("[1] - Caminho vermelho")
    print("[2] - Caminho preto")
    caminho = int(input())


interação = 1

while interação < 7:

    salas("1")
    interação += 1

else:
    print("Você e sua guilda se perderam na dungeon e acabaram morrendo pelas criaturas místicas que viviam nela!")
    print("GGGGG   AAA   M   M  EEEEE      OOO   V   V  EEEEE  RRRR")
    print("G      A   A  MM MM  E         O   O  V   V  E      R   R")
    print("G GGG  AAAAA  M M M  EEEEE     O   O   V V   EEEEE  RRRR")
    print("G   G  A   A  M   M  E         O   O   V V   E      R  R")
    print("GGGGG  A   A  M   M  EEEEE      OOO     V    EEEEE  R   R")
