soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma dos números ímpares e múltiplos de 3 entre 1 e 500 é:',soma)
print('o número de termos ímpares e múltiplos de 3 entre 1 e 500 é:',cont)
