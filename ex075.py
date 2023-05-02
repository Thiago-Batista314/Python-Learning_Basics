a = int(input('Digite um número:'))
b = int(input('Digite um número:'))
c = int(input('Digite um número:'))
d = int(input('Digite um número:'))
exer = (a, b, c, d)
if 3 in exer:
    print(exer.index(3)+1)
print(exer, exer.count(9),)
par = 0
for n in exer:
    if n % 2 == 0:
        par += 1
print(par)
