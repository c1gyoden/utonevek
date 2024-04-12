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

lista = []

for sor in fajl:
    sor = sor.strip().split(';')
    for adat in sor:
        if adat == '':
            sor[sor.index(adat)] = '-'
            
    lista.append(Utonev(sor[0], sor[1], sor[2], sor[3], sor[4], sor[5]))

for a in lista:
    print(a)

    