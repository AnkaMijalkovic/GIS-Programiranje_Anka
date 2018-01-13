### OSOBA ###
# Osoba
class Osoba:
    def __init__(self, *atributi):
        self.ime = input('unesite ime:')
        self.prezime = input('unesite prezime:')
        self.dat_rodj = input('unesite dat_rodj:')
        self.adresa = input('unesite adresu:')

    def __str__(self):
        return 'Podaci o osobi: \n Ime: {:s} \n Prezime {:s} \n Datum rodjenja: {:s} \n Adresa stanovanja {:s}'. \
            format(self.ime, self.prezime, self.dat_rodj, self.adresa)

    def daj_dat_rodj(self):
        return 'Datum rodjenja: {0:s}'.format(self.dat_rodj)


### DjAK ###
class Djak(Osoba):
    def __init__(self, *atributi):
        Osoba.__init__(self, *atributi)
        self.naziv_skole = input('Unesite naziv skole:')
        self.odeljenje = input('Unesite odeljenje, u formi odeljenje-razred:')
        self.god_upisa = input('Unesite godinu upisa skole:')

    def __str__(self):
        return Osoba.__str__(self) + '\n Naziv skole: {:s} \n Odeljenje: {:s} \n Godina upisa skole: {:s}'. \
            format(self.naziv_skole, self.odeljenje, self.god_upisa)

    def daj_naziv_skole(self):
        return 'Naziv skole je: {0:s}'.format(self.naziv_skole)

    def daj_odeljenje(self):
        return 'Odeljenje {0:s}'.format(self.odeljenje)

    def daj_god_upisa(self):
        return self.god_upisa

    def postavi_naziv_skole(self,skola):
        self.naziv_skole = skola

    def postavi_odeljenje(self, odelj):
        self.odeljenje = odelj

    def postavi_god_upisa(self,g_u):
        self.god_upisa = g_u

    def koji_razred(self):
        raz = str(self.odeljenje)
        raz_split = raz.split('-')
        razr = raz_split[1]
        return razr

    def da_li_je_obnovio_razred(self):
        tek_god = input('Unesite vrednost tekuce godine, u formi xxxx')
        recnik = {'1':7, '2':8, '3':9, '4':10, '5':11, '6':12, '7':13, '8':14}
        god_rodj = str(self.daj_dat_rodj())
        god_rodj1 = god_rodj.split('.')
        god_rodj2 = god_rodj1[2]
        aa = int (self.daj_god_upisa())-int(god_rodj2)
        if aa == 7:
            a1 = int(tek_god) - int(god_rodj2)
            a2 = self.koji_razred()
            a3 = recnik[a2]
            if a1 == a3:
                print "Nije ponavljao."
            else:
                print "ponavljao je!"

        else:
            print 'proverite godinu upisa'





### ZAPOSLENI ###

class Zaposleni(Osoba):
    def __init__(self, lista_kompanija=[], lista_zakljucenja=[], lista_prekida=[], *atributi):
        Osoba.__init__(self, *atributi)
        self.naziv_komp = input('Unesite naziv trenutne kompanije:')
        self.dep = input('Unesite naziv departmana:')
        self.lista_kompanija = lista_kompanija
        self.lista_zakljucenja = lista_zakljucenja
        self.lista_prekida = lista_prekida
        self.br_komp = input(
            'Unesite broj kompanija u kojima je zaposleni prethodno radio (ne racunajuci trenutnu kompaniju, ako je zaposljen):')
        self.trenutno_zap = input('Unesite datum zakljucenja trenutnog zaposlenja (ako postoji):')
        self.trenutni_pr = input('Unesite danasnji datum ukolike je zaposleni u radnom odnosu:')

        i = 0
        while i < self.br_komp:
            kompanija = input('Unesite kompaniju')
            lista_kompanija.append(kompanija)
            zakljucenje = input('Unesite datum zakljucenja')
            lista_zakljucenja.append(zakljucenje)
            prekid = input('Unesite datum prekida')
            lista_prekida.append(prekid)
            i += 1
        print 'Kompanije:', lista_kompanija
        print 'Datumi zakljucenja:', lista_zakljucenja
        print 'Datumi prekida:', lista_prekida

    def radniStaz(self):
        dani_zaklj = []
        meseci_zaklj = []
        godine_zaklj = []
        q = 0
        while q < len(self.lista_zakljucenja):
            zaklj_split = self.lista_zakljucenja[q].split('.')
            dani_zaklj.append(int(zaklj_split[0]))
            meseci_zaklj.append(int(zaklj_split[1]))
            godine_zaklj.append(int(zaklj_split[2]))
            q += 1

        dani_prekida = []
        meseci_prekida = []
        godine_prekida = []
        q1 = 0
        while q1 < len(self.lista_prekida):
            prekid_split = self.lista_prekida[q1].split('.')
            dani_prekida.append(int(prekid_split[0]))
            meseci_prekida.append(int(prekid_split[1]))
            godine_prekida.append(int(prekid_split[2]))
            q1 += 1

        dl = 0
        dani_lista = []
        while dl < len(dani_zaklj):
            dani_lista.append(abs(dani_prekida[dl] - dani_zaklj[dl]))
            dl += 1

        meseci_lista = []
        ml = 0
        while ml < len(meseci_zaklj):
            meseci_lista.append(abs(meseci_prekida[ml] - meseci_zaklj[ml]))
            ml += 1

        godine_lista = []
        gl = 0
        while gl < len(godine_zaklj):
            godine_lista.append(abs(godine_prekida[gl] - godine_zaklj[gl]))
            gl += 1

        tren_z_split = self.trenutno_zap.split('.')
        dz = int(tren_z_split[0])
        mz = int(tren_z_split[1])
        gz = int(tren_z_split[2])
        tren_p_split = self.trenutni_pr.split('.')
        dp = int(tren_p_split[0])
        mp = int(tren_p_split[1])
        gp = int(tren_p_split[2])
        trenutna_komp_staz = (abs(dp - dz) / 30) + abs(mp - mz) + (abs(gp - gz) * 12)

        return (sum(dani_lista) / 30) + (sum(meseci_lista)) + (sum(godine_lista) * 12) + trenutna_komp_staz


zap1 = Zaposleni()
zap1.radniStaz()

dj = Djak()

dj.koji_razred()
dj.da_li_je_obnovio_razred()