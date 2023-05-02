from math import sin, cos, tan, radians
an = float(input('Digite o ângulo:'))
an1 = radians(an)
s = sin(an1)
c = cos(an1)
t = tan(an1)
print('Para esse ângulo temos:\nO seno vale {:.2f}\nO cosseno vale {:.2f}\nA tangente vale {:.2f}'.format(s, c, t))
