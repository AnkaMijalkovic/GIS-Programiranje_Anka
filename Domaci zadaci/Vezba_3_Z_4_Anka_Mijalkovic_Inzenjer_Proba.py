
from Vezba_3_Z_4_Anka_Mijalkovic_Inzenjer import Inzenjer
from Vezba_3_Z_4_Anka_Mijalkovic_Inzenjer import GeodetskiInzenjer
from Vezba_3_Z_4_Anka_Mijalkovic_Inzenjer import ElektrotehnickiInzenjer


##### Proba #####

inz1 = Inzenjer('anka', 'mij', 65465, 'asdvf')
print inz1

    # get metode
print inz1.daj_ime()
print inz1.daj_prezime()
print inz1.daj_jmbg()
print inz1.daj_licencu()
   # set metode
inz0 = Inzenjer()
inz0.postavi_ime("aaaaaa")
inz0.postavi_prezime("bbbbb")
inz0.postavi_maticni_broj(77777)
inz0.postavi_licencu('ccccc')
print inz0

#### geodetski inzenjer #####
gi = GeodetskiInzenjer()
print gi
   # getter
print gi.daj_ime()
print gi.daj_prezime()
print gi.daj_jmbg()
print gi.daj_licencu()
print gi.daj_br_god_rs()
   #setter
gi.postavi_ime("ankaaaaa")
gi.postavi_prezime("mijalkovicccc")
gi.postavi_maticni_broj(123456789)
gi.postavi_licencu('')
gi.postavi_br_god_rs(4)
print gi

# da li inz ima licencu

gi.da_li_ima_licencu()

### elektrotehnicki inz ###

ei = ElektrotehnickiInzenjer()
print ei

   # getter
print ei.daj_ime()
print ei.daj_prezime()
print ei.daj_jmbg()
print ei.daj_licencu()
print ei.daj_br_proj()
   #setter
ei.postavi_ime("ankaaaaa")
ei.postavi_prezime("mijalkovicccc")
ei.postavi_maticni_broj(123456789)
ei.postavi_licencu('/')
ei.postavi_br_proj(4)
print ei
   # da li ima licencu
ei.da_li_ima_licencu()
