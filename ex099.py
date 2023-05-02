from random import randint as rand
lista = []
cont = 0


def maior(lst):
    print('-='*25)
    print('ANALISANDO VALORES...')
    print('-=' * 25)
    print('Os valores passados foram:', lst)
    mai = cont = 0
    for valor in lst:
        if valor > mai:
            mai = valor
        cont += 1
    print('Ao todo foram passados {} valores.'.format(cont))
    print('O maior informado foi: ', mai)
    print()


for v in range(0, rand(0, 20)):
    for c in range(0, rand(0, 20)):
        num = rand(0, 100)
        lista.append(num)
    cont += 1
    maior(lista)
    lista.clear()

print()
print('Ao total, analisei valores {} vezes.'.format(cont))
