num = cont = soma = 0
while True:
    num = int(input('Digite um número:'))
    if num == 999:
        break
    cont += 1
    soma += num
print(soma, cont)
