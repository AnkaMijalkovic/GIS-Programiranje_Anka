
##### Test ######
from Vezba_3_Z_2_Anka_Mijalkovic_Geometrija import Tacka
from Vezba_3_Z_2_Anka_Mijalkovic_Geometrija import Duz
import gc


x_p = input('unesi xp')
y_p = input('unesi yp')
x_k = input('unesi xk')
y_k = input('unesi yk')

tacka_p = Tacka(x_p, y_p)
tacka_k = Tacka(x_k, y_k)
duz_1 = Duz(tacka_p, tacka_k)

# Kreiranje druge duzi
druga_duz = Duz(Tacka(0,0), Tacka(0,5))
druga_duz1 = druga_duz.kreiraj_duz(0,0,0,7)

# Stampa sve postojece duzi
for obj in gc.get_objects():
    if isinstance(obj, Duz):
        print obj


# stampa memoriju (ispravi)
#lista_duzina_svih_duzi = []
#for obj in gc.get_objects():
#    if isinstance(obj, Duz):
#        lista_duzina_svih_duzi.append(obj.duzina())
#print lista_duzina_svih_duzi



# pomeraj krajnje tacke
ttpp = Tacka(0,1)
ttkk = Tacka(2,3)
duz_2 = Duz(ttpp, ttkk)
print duz_2
x_pomeraj = input('unesite pomeraj dx za krajnju tacku')
y_pomeraj = input('unesite dy pomeraj za krajnju tacku')
duz_2_pomerena = Duz(ttpp, ttkk.pomeranje(x_pomeraj,y_pomeraj))
print duz_2_pomerena


