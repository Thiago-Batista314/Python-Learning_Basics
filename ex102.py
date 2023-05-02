def fatorial(n, show=False):
    """
    :param n: Number for factorial;
    :param show: If you want to show the operation;
    :return: return the result of factorial of n;
    """
    print('-=' * 15)
    cont = 0
    for c in range(1, n):
        n *= c
        cont += 1
    if show:
        v = cont + 1
        while v >= 0:
            print('{} '.format(v), end='')
            v -= 1
            if v == 0:
                print('=', n)
                break
            print('x', end=' ')
    else:
        return n


resp = fatorial(7, True)
if resp == None:
    print()
else:
    print(resp)
