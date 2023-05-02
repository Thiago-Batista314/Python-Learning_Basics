n = int(input('Digite um número para verificar se ele é primo:'))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        cont = cont + 1
if cont == 2:
    print('\nEle é primo!!!')
else:
    print('\nEle não é primo!!!')
