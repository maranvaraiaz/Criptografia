import fileinput

lines = []
aux=0
for line in fileinput.input():
    lines.append(line)
    if (lines!=''):
        if (line.find('.')>=0):
            aux+=float(line)
        else:
            aux+=int(line)
    print(aux)
