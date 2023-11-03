s = 0
for c in range(0, 501, 3):
    if(c % 2 == 1):
        imp = c
        if(imp % 3 == 0):
            mult = imp
            s += mult

print('A somatora total será de {:.2f}'.format(s))