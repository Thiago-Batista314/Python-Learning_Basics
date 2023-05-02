import random
aa = str(input('Aluno 1:'))
ab = str(input('Aluno 2:'))
ac = str(input('Aluno 3:'))
ad = str(input('Aluno 4:'))
esc = [aa, ab, ac, ad]
random.shuffle(esc)
print('A ordem dos alunos é:')
print(esc)
