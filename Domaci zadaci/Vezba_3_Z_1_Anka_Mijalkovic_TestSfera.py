import gc

from Vezba_3_Z_1_Anka_Mijalkovic_Sfera import Sfera

print Sfera.broj_sfera()

sfera = Sfera(4,0,0,0)
globus = Sfera(12,1.0,1.0,1.0)
bilijarska_lopta = Sfera(10,10,0)
jedinicna_sfera = Sfera(1,0,0,0)

print Sfera.broj_sfera()

lista_svih_sfera = []
for obj in gc.get_objects():
    if isinstance(obj, Sfera):
        lista_svih_sfera.append(obj)
print len(lista_svih_sfera)


lista_zapremina = []
for i in lista_svih_sfera:
    lista_zapremina.append(i.zapremina())
print lista_zapremina


# brisanje svih instanci u klasi Sfera (ne radi..)
#for obj in gc.get_objects():
#    if isinstance(obj, Sfera):
 #       del obj






