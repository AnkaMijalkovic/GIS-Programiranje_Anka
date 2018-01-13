# Zadatak 1 (Vezba 2)

niz1 = input("Unesite niz: (npr. 1,2,3)")
niz2 = [17,45,78,65, 48]
niz3 = [1,2,3,4]

sump = 0
for i in niz1:
    if i%2==0:
        sump += i
print 'Suma parnih elemenata niza je:', sump
