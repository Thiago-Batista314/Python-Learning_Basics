#Fórmula: Fn = Fn-1 + Fn-2
fibonacci = int(input('Quantos termos você quer ver?'))
t1 = 0
t2 = 1
cont = 3
print(t1,'=>', t2, end=' => ')
while cont <= fibonacci:
    t3 = t1 + t2
    print(t3, end=' => ')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim')
