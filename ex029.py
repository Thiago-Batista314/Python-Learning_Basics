import random
vel = random.choice(range(70, 90))
print('A velocidade que você passou foi:',vel)
if vel >= 80:
    multa = (vel - 80) * 7
    print('''Por passar acima do limite,
irás tomar uma multa de R${} '''.format(multa))
