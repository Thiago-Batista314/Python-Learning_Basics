lista = []
pergunta = 'S'
valor = 0
while pergunta == 'S':
    valor = int(input('Digite um valor:'))
    if valor in lista:
        print('Valor Duplicado!')
    if valor not in lista:
        lista.append(valor)
    pergunta = str(input('Quer continuar [S/N]?')).upper().strip()
lista.sort()
print(lista)
