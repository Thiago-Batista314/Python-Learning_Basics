from math import factorial
n = int(input('Digite um número para ver seu fatorial:'))
print('Digite 0 para sair do programa.')
while n != 0:
    print('Seu fatorial é ', factorial(n))
    n = int(input('Quer ver de algum outro número?'))
print('Acabou com sucesso!!!')
