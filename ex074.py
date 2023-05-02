from random import randint
a = randint(0,10)
b = randint(0,10)
c = randint(0,10)
d = randint(0,10)
e = randint(0,10)
num = (a,b,c,d,e)
maior = menor = 0
for n in num:
    print(n,end=' ')
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print('\n', maior,menor)
