num = (0,'zero',1, 'um', 2, 'dois', 3,'três', 4, 'quatro', 5,'cinco', 6,'seis',7,'sete',
8,'oito',9,'nove',10,'dez',11,'onze',12,'doze',13,'treze',14,'quatorze',15,'quinze',16,'dezesseis',
17,'dezesete',18,'dezoito',19,'dezenove',20,'vinte')

ver = 'S'

while ver == 'S':

    n = int(input('Digite um número entre 0 e 20:'))

    vis = num[n*2+1]

    print('O número que você digitou foi', vis)

    ver = str(input('[S/N]?')).upper().strip()