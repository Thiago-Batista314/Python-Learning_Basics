def leia_int(pergunta='Digite um número inteiro:', num=0, distancia=0):
    while True:
        try:
            num = int(input(pergunta))

        except (ValueError, TypeError):
            print('\033[31mERRO!: Digite um número inteiro válido!\033[m')
            continue

        except KeyboardInterrupt:
            print('\033[31mO Usuário preferiu encerrar o programa!\033[m')
            return 0

        if distancia:
            if num not in range(1, distancia+1):
                print('\033[31mOpção inválida!\033[m')
                continue
            else:
                break
        else:
            break

    return num


def leia_float(num=''):
    while True:
        try:
            num = str(input('Digite um número real:')).replace(',', '.')
            float(num)
        except (ValueError, TypeError):
            print('\033[31mERRO!: Digite um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO Usuário preferiu encerrar o programa!\033[m')
            return 0
        else:
            break
    return float(num)


def leia_string(string):
    while True:
        try:
            string = str(input(string))
        except (ValueError, TypeError):
            print('\033[31mERRO!: Digite um valor válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO Usuário preferiu encerrar o programa!\033[m')
            return 0
        while string.isnumeric():
            print('\033[31mERRO!: Digite um nome válido!\033[m')
            string = str(input('Nome:'))
        else:
            break
    return string
