class Utonev:
    def __init__(self, nev, elso, masodik, ujsz1, ujsz2, nem):
        self.nev = nev
        self.elso = elso
        self.masodik = masodik
        self.ujsz1 = ujsz1
        self.ujsz2 = ujsz2
        self.nem = nem

    def __str__(self):
        return f'Név: {self.nev}\nElső: {self.elso}\nMásodik: {self.masodik}\nUjsz1: {self.ujsz1}\nUjsz2: {self.ujsz2}\nNem: {self.nem}\n'

fajl = open('utonev.txt', 'rt', encoding='ansi')
fajl.readline()

lista = []

for sor in fajl:
    sor = sor.strip().split(';')
    for adat in sor:
        if adat == '':
            sor[sor.index(adat)] = '-'

    lista.append(Utonev(sor[0], sor[1], sor[2], sor[3], sor[4], sor[5]))

for a in lista:
    print(a)

print(len(lista), 'név adatai van a listában')

ferfiak = 0
nok = 0
ujszfiuk = 0
ujszlanyok = 0
for n in lista:
    if n.elso != '-':
        if n.nem == 'F':
            ferfiak += int(n.elso)

        else:
            nok += int(n.elso)

    if n.ujsz1 != '-':
        if n.nem == 'F':
            ujszfiuk += int(n.ujsz1)
        else:
            ujszlanyok += int(n.ujsz1)

    if n.ujsz2 != '-':
        if n.nem == 'F':
            ujszfiuk += int(n.ujsz2)
        else:
            ujszlanyok += int(n.ujsz2)


print(ferfiak, "személynek van férfi neve")
print(nok, "személynek van női neve")
print("Az ország népessége", ferfiak + nok, "fő\n")

print(ujszfiuk, 'újszülött fiú van')
print(ujszlanyok, 'újszülött lány van')
