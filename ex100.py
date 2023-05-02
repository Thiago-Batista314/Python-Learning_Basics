from random import randint as r
from time import sleep as wait
lista = []


def sorteia(lst):
    print('Sorteando valores:', end='')
    for c in range(0, 5):
        lst.append(r(0, 10))
        print(lst[c], end=' ')
        wait(0.375)
    print('PRONTO!')


def soma_par(lst):
    soma = 0
    for v in lst:
        if v % 2 == 0:
            soma += v
    print('A soma dos valores pares é:', end='')
    print(soma)


sorteia(lista)
soma_par(lista)
