from random import randint
vit = 0

while True:
    jog = int(input('Digite um valor:'))
    esc = str(input('Quer par ou ímpar [P/I]?')).upper().strip()
    comp = randint(1, 10)

    if esc == 'P':
        if (jog + comp) % 2 != 0:
            print('Você \033[31mperdeu\033[m.')
            print('O computador jogou', comp)
            print('O total deu', jog + comp)
            break

        if (jog + comp) % 2 == 0:
            print('O computador jogou', comp)
            print('O total deu', jog + comp)
            print('VOCÊ \033[33mVENCEU\033[m!!! Vamos jogar novamente...')
            vit += 1
            print('-='*20)

    if esc == 'I':
        if (jog + comp) % 2 != 0:
            print('O computador jogou', comp)
            print('O total deu', jog + comp)
            print('VOCÊ \033[33mVENCEU\033[m!!! Vamos jogar novamente...')
            vit += 1
            print('-='*20)

        if (jog + comp) % 2 == 0:
            print('Você \033[31mperdeu\033[m.')
            print('O computador jogou', comp)
            print('O total deu', jog + comp)
            break
if 0<= vit <= 1:
    print('Você venceu \033[33m{}\033[m partida.'.format(vit))
else:
    print('Você venceu \033[33m{}\033[m partidas.'.format(vit))
