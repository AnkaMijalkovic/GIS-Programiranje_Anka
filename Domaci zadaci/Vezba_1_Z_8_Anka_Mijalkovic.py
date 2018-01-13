# Zadatak 8 (Vezba 1)

import random

tacanbroj = random.randint(0, 100)

ime = raw_input('Unesite svoje ime')
broj = input('Unesite broj u intervalu [0, 100]:')  # prvi pokusaj
if broj > tacanbroj:
    print 'Uneli ste veci broj od tacnog broja'
elif broj < tacanbroj:
    print 'Uneli ste manji broj od tacnog broja'
else:
    pass

i=1 #brojac krece od 1 zbog prvog pokusaja
while broj != tacanbroj:  #ostala pogadjanja
    broj = input('Unesite novi broj:')
    if broj > tacanbroj:
        print 'Uneli ste veci broj od tacnog broja'
    else:
        print 'Uneli ste manji broj od tacnog broja'
    i += 1
else:
    print 'Pogodili ste broj u', i ,'pokusaju'





