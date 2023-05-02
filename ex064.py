num = 1
n = 0
num = int(input('Digite um número [999 para parar]:'))
soma = 0
while num != 999:
    soma += num
    n += 1
    num = int(input('Digite um número [999 para parar]:'))
print(soma, n)
