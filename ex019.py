from random import choice
a1 = str(input('O aluno 1:'))
a2 = str(input('O aluno 2:'))
a3 = str(input('O aluno 3:'))
a4 = str(input('O aluno 4:'))
esc = [a1, a2, a3, a4]
esc1 = choice(esc)
print('O aluno escolhido foi: {}'.format(esc1))

