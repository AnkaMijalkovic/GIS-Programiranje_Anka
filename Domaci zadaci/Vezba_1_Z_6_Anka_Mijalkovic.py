# Zadatak 6 (Vezba 1)

kar5 = raw_input('Unesite pet karaktera, npr. a4r5f')
while len(kar5)!=5:
    kar5 = raw_input('Unesite tacno pet karaktera')


listakar = []
for i in kar5:
    if i.isdigit():
        listakar.insert(0, i)
print len(listakar)
