from random import randint
lista = []
lista_impares = []
lista_pares = []
res = 's'
while res == 's':
    num = randint(0, 100)
    res = str(input('[S/N]'))
    lista.insert(0, num)
    if num % 2 == 0:
        lista_pares.insert(0, num)
    else:
        lista_impares.insert(0, num)
print(lista)
print(lista_pares)
print(lista_impares)
