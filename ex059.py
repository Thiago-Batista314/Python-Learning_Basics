num1 = int(input('Digite algum número:'))
num2 = int(input('Digite outro número:'))

print('Escolha alguma das opções abaixo:')
print('[ 1 ] Somar')
print('[ 2 ] Multiplicar')
print('[ 3 ] Verificar qual é o maior')
print('[ 4 ] Colocar novos números')
print('[ 5 ] Sair do programa')
menu = 0

while menu != 5:
    menu = int(input('O que deseja fazer?'))
    if menu < 5:
        if menu == 1:
            print('A soma entre {} e {} é {}'.format(num1, num2, num1+num2))

        elif menu == 2:
            print('A multiplicação entre {} e {} é {}'.format(num1, num2, num1*num2))

        elif menu == 3:
            if num1 > num2:
                print('O primeiro número é o maior.')

            elif num1 < num2:
                print('O segundo número é maior.')

            else:
                print('Os dois são iguais.')

        elif menu == 4:
            num3 = int(input('Digite algum valor numérico:'))
            num4 = int(input('Digite outro valor numérico:'))

    if menu > 5:
        print('Valor inválido.')

print('Código finalizado com sucesso!!!')
