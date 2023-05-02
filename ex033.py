num1 = input('Digite um valor:')
num2 = input('Digite outro valor:')
num3 = input('Mais um ainda:')
if num1 < num2 and num1 < num3:
    menor = num1
    print('o menor número é', num1)
if num2 < num1 and num2 < num3:
    menor = num2
    print('o menor número é', num2)
if num3 < num1 and num3 < num2:
    menor = num3
    print('o menor número é', num3)
if num1 > num2 and num1 > num3:
    maior = num1
    print('o maior número é', num1)
if num2 > num1 and num2 > num3:
    maior = num2
    print('o maior número é', num2)
if num3 > num1 and num3 > num2:
    maior = num3
    print('o maior número é', num3)
