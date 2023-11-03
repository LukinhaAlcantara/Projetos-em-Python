def fatorial(n, show):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else :
                print(' = ', end='')
        f *= c
    return f


fatorial(
    n = int(input('Digite o numero para ver seu fatorial: ')),
    show = str(input('Deseja ver o fatorial? SIM=True NAO=False')).title()
)