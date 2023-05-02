def leia_int(pergunta='Digite um número inteiro:', num=0, distancia=0):
    while True:
        # Tenta perguntar um número;
        try:
            num = int(input(pergunta))

        # Mostra se há erro no valor digitado
        except (ValueError, TypeError):
            print('\033[31mERRO!: Digite um número inteiro válido!\033[m')
            continue

        # Mostra se o úsuario não quis digitar o número;
        except KeyboardInterrupt:
            print('\033[31mO Usuário preferiu encerrar o programa!\033[m')
            return 0

        # Se houver a distância, faz a verificação se o valor está dentro da distância;
        if distancia:
            if num not in range(1, distancia+1):
                print('\033[31mOpção inválida!\033[m')
                continue
            else:
                break
        else:
            break
    # Retorna o número digitado já tratado;
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


def veririficar_nome(nome):
    # Armazena o nome numa lista, onde os nomes à partir da posição 2,
    # Ou seja, do 3 em diante sejam colocados como uma posição só na lista;
    lista = nome.split(maxsplit=3)

    # Verifica se a lista do nome tem mais de três posições e exclui a última;
    if len(lista) > 3:
        lista.pop(len(lista)-1)

    nome2 = ''

    # Verifica se a última posição da lista é de, da, ou do,
    # para melhorar a visualização no arquivo;
    if 'd' in lista[-1].lower():
        lista.pop(len(lista)-1)

    for name in lista:
        nome2 += str(name + ' ').capitalize()

    return nome2


def verificar_arquivo(nomearquivo):
    try:
        a = open(nomearquivo)
        a.close()
        print('Arquivo encontrado!')

    except (FileExistsError, FileNotFoundError):

        try:
            c = open(nomearquivo, 'wt+')
            c.write(f'{"PESSOAS":^7}')
            c.write(f'{"IDADES":>30}\n')
            c.write('')
            c.close()
            print('Arquivo criado e salvo!')

        except:
            print('Não consegui criar o arquivo!')
