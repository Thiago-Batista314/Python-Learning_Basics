from time import sleep
from ex115.trat_valores_arquivos import *


def titulo(msg, cor=''):
    tam = len(msg)+10

    print('=='*tam)
    print(f'{cor}{msg.center((tam-2)*2)}\033[m')
    print('=='*tam)

    sleep(0.5)


def opções(dicionario, retorno, kn):

    dicionario[kn] = retorno

    return dicionario[kn]


def respostas():
    print('\033[33m1 -\033[m \033[34mVer pessoas cadastradas;\033[m')
    print('\033[33m2 -\033[m \033[34mCadastrar nova pessoa;\033[m')
    print('\033[33m3 -\033[m \033[34mFinalizar o Programa;\033[m')


def menu():
    # verificação se existe o arquivo, e, se existir acessa-o;
    verificar_arquivo('cadastrados.txt')
    arquivo = open('cadastrados.txt')
    arquivo.close()

    respostas()
    dicionario = {}
    while True:
        sleep(1)
        print('==' * 24)
        resposta = str(leia_int('\033[33mOpção:\033[m', distancia=3))
        print('=='*24)
        sleep(1)

        if resposta == '1':
            opções(dicionario, exibir(), resposta)
            dicionario.clear()
            print('==' * 24)
            respostas()
            continue

        if resposta == '2':
            opções(dicionario, cadastrar(), resposta)
            dicionario.clear()
            print('==' * 24)
            respostas()
            continue

        if resposta == '3':
            opções(dicionario, finalizar(), resposta)
            dicionario.clear()
            break
    arquivo.close()


def exibir():
    arquivo = open('cadastrados.txt', 'r')
    todo = arquivo.read()
    titulo('PESSOAS CADASTRADAS')
    print(todo)
    arquivo.close()


def cadastrar():
    arquivo = open('cadastrados.txt', 'a')
    titulo('CADASTRAR NOVA PESSOA')

    # cria as variáveis a verifica se elas estão corretas;
    nome = leia_string('Nome:')
    idade = leia_int('Idade:')
    nomevdd = veririficar_nome(nome)

    # armazena as variáveis no arquivo e fecha-o;
    arquivo.write(f'{nomevdd:<20}')
    arquivo.write(f'\t\t{idade} anos\n')


def finalizar():
    titulo('Até Logo! Finalizando...')
