import sys
aux=0
while (1):
    a = sys.stdin.readline()
    if (a!=''):
        if (a.find('.')>=0):
            aux+=float(a)
        else:
            aux+=int(a)
    else:
        print(aux)
        break
