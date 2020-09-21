
alfabeto = ('abcdefghijklmnopqrstuvxyz')

print('1 - Criptografar, \n'
          '2 - Decriptografar, \n'
          '3 - Brute Force, \n'
          '4 - Finalizar.')
menu = input("Digite uma opção:")

if menu == '1':
    mensagem = input("Digite uma mensagem:")
    rotacao = int(input("Digite um numero inteiro para rotação:"))
    mensagemCifrada = ''

    for letra in mensagem:
        if letra not in alfabeto:
            mensagemCifrada += letra
        else:
            posicao = alfabeto.index(letra)
            mensagemCifrada += alfabeto[(posicao + int(rotacao)) % len(alfabeto)]

    print(mensagemCifrada)

elif menu == '2':
    mensagem = input("Digite a mensagem criptografada, feita anteriormente:")
    rotacao = int(input("Digite o mesmo número utilizado anteriormente para rotacionar:"))
    mensagemCifrada = ''

    for letra in mensagem:
        if letra not in alfabeto:
            mensagemCifrada += letra
        else:
            posicao = alfabeto.index(letra)
            mensagemCifrada += alfabeto[(posicao - int(rotacao)) % len(alfabeto)]
    print(mensagemCifrada)

elif menu == '3':
    mensagem = input("Digite a mensagem criptografada:")
    rotacao = 0
    mensagemDecifrada = ''
    while rotacao < 27:
        for letra in mensagem:
            if letra not in alfabeto:
                mensagemDecifrada += letra
            else:
                posicao = alfabeto.index(letra)
                mensagemDecifrada += alfabeto[posicao - rotacao]

        print(f'{mensagemDecifrada}, {rotacao}')
        mensagemDecifrada = ''
        rotacao += 1
elif menu == '4':
    exit