import random
num = random.choice(range(100))
par = num % 2
print('o número escolhido foi:', num)
if par == 0:
    print('{} é par'.format(num))
else:
    print('{} é ímpar'.format(num))
