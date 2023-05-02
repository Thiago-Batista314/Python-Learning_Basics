lista = []
resposta = 'S'
while resposta == 'S':
    n = int(input('Digite um número:'))
    lista.append(n)
    resposta = str(input('Quer continuar [S/N]?')).upper().strip()
if 5 in lista:
    print('O 5 faz parte da lista.')
else:
    print('O 5 não foi encontrado na lista.')
print('Você digitou {} elementos.'.format(len(lista)))
lista.sort(reverse=True)
print('A lista em ordem decrescente é {}'.format(lista))
