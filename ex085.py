pares = []
impares = []
lista = [pares, impares]

for c in range(0, 7):
    num = int(input('Digite o {}º número:'.format(c+1)))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

pares.sort()
impares.sort()

print('Os números pares digitados foram {}.'.format(pares[:]))
print('Os números impares digitados foram {}.'.format(impares[:]))
