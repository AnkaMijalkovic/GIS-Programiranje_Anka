#

class Inzenjer:
    def __init__(self, ime = 'Anka', prezime = 'Mijalkovic', jmbg = 1233, licenca = 'aa'):
        self._ime = ime
        self._prezime = prezime
        self._jmbg = jmbg
        self._licenca = licenca
    def __str__(self):
        return 'Podaci o inzenjeru: \n Ime inzenjera: {:s} \n Prezime inzenjera: {:s} \n Maticni broj lica: {:d} \n Licenca: {:s} '\
            .format(self._ime, self._prezime, self._jmbg, self._licenca)
    # Getter metode
    def daj_ime(self):
        return 'Ime inzenjera: {:s}'.format(self._ime)
    def daj_prezime(self):
        return 'Prezime inzenjera: {:s}'.format(self._prezime)
    def daj_jmbg(self):
        return 'Maticni broj lica: {:d}'.format(self._jmbg)
    def daj_licencu(self):
        return 'Licenca: {:s}'.format(self._licenca)
    # Setter metode
    def postavi_ime(self, ime):
        self._ime = ime
    def postavi_prezime(self, prezime):
        self._prezime = prezime
    def postavi_maticni_broj(self, jmbg):
        self._jmbg = jmbg
    def postavi_licencu(self, licenca):
        self._licenca = licenca

# Geodetski inzenjer
class GeodetskiInzenjer(Inzenjer):

    def __init__(self , ime = 'Anka', prezime = 'Mijalkovic', jmbg = 1233, licenca = 'aa' , br_god_rs = 0):
        Inzenjer.__init__(self, ime , prezime , jmbg , licenca )
        self._br_god_rs = br_god_rs

    def __str__(self):
        return Inzenjer.__str__(self) + (' \n Broj godina radnog staza: {:d}'.format(self._br_god_rs))

    def daj_br_god_rs(self):
        return 'Broj godina radnog staza: {:d}'.format(self._br_god_rs)

    def postavi_br_god_rs(self, br_god_rs):
        self._br_god_rs =  br_god_rs

    def da_li_ima_licencu(self):
        if self._licenca == '':
            print 'Inzenjer nema licencu'
        elif self._licenca == '/':
            print 'Inzenjer nema licencu'
        else:
            print 'Inzenjer ima licencu: {:s}'.format(self._licenca)

# Elektrotehnicki Inzenjer
class ElektrotehnickiInzenjer(Inzenjer):
    def __init__(self , ime = 'Anka', prezime = 'Mijalkovic', jmbg = 1233, licenca = 'aa' , br_proj = 0):
        Inzenjer.__init__(self , ime , prezime , jmbg , licenca  )
        self._br_proj = br_proj
    def __str__(self):
        return Inzenjer.__str__(self) + ('\n Broj projekata na kojima je radio: {:d}'.format(self._br_proj))
    def postavi_br_proj(self, br_proj):
        self._br_proj = br_proj
    def daj_br_proj(self):
        return 'Broj projekata na kojima je radio: {:d}'.format(self._br_proj)
    def da_li_ima_licencu(self):
        if self._licenca == '':
            print 'Inzenjer nema licencu'
        elif self._licenca == '/':
            print 'Inzenjer nema licencu'
        else:
            print 'Inzenjer ima licencu: {:s}'.format(self._licenca)


