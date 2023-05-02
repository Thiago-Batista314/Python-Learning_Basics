import random
jog = input('Pensei num número de 0 a 5.\n'
            'Tente advinhá-lo!')
a = '0'
b = '1'
c = '2'
d = '3'
e = '4'
f = '5'
esc = [a, b, c, d, e, f]
cpu = random.choice(esc)
if jog == cpu:
    print('Acertou!!!')
else:
    print('Não foi dessa vez ;-;')
    print('O número que escolhi foi', cpu)
