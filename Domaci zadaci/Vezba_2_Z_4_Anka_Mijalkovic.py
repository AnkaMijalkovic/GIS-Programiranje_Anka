# Zadatak 4 (Vezba 2)

from itertools import chain
niz11 = input("Unesite prvi niz:")
niz22 = input("Unesite drugi niz:")

novi_niz = []
a1 = "p"
a2 = "d"
a = raw_input('Ako zelite da se prvo redjaju elementi niza "niz1" unesite "p", a ako zelite da se prvo redjaju elementi naiza'
          '"niz2", unesite "d" ')
if a == a1:
    novi_niz = list(chain(*zip(niz11, niz22)))
    print novi_niz
elif a == a2:
    novi_niz = list(chain(*zip(niz22, niz11)))
    print novi_niz
else:
    print 'morate uneti "p" ili "d"'





