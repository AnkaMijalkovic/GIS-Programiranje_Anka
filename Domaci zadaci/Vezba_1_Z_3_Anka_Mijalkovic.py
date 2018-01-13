# Zadatak 3 (Vezba 1)
import math

#unosenje PRVOG pravca u trazenom obliku
pravac1 = raw_input("Unesite prvi pravac:" ).split(':')

#unosenje DRUGOG pravca u trazenom obliku
pravac2 = raw_input("Unesite drugi pravac:" ).split(':')

#izdvajanje elemenata liste u zasebne promenljive za prvi pravac i
# konverzija promenljivih iz stringa u int i float za prvi pravac
stepeni1 = int( pravac1[0])
while stepeni1 in range(0, 360):
    stepeni1 = stepeni1
    break
else:
    stepeni1 = raw_input("Unesite ponovo stepene za prvi pravac ")
    stepeni1 = int(stepeni1)

minuti1 = int(pravac1[1])
while minuti1 in range(0, 60):
    minuti1 = minuti1
    break
else:
    minuti1 = raw_input("Unesite ponovo minute za prvi pravac ")
    minuti1 = int(minuti1)

sekunde1 = int(pravac1[2])
while sekunde1 in range(0, 60):
    sekunde1 = sekunde1
    break
else:
    sekunde1 = raw_input("Unesite ponovo sekunde za prvi pravac ")
    sekunde1 = int(sekunde1)


#Provera (ukloniti komentar)
# print stepeni1, minuti1, sekunde1
#Prevodjenje u decimalni zapis
dec1 = stepeni1 + minuti1/60.0 + sekunde1/3600.0 #mora se napisati 60.0 i 3600.0 jer ako se deli sa int onda je i rezultat int
#Provera (ukloniti komentar)
# print dec1

#izdvajanje elemenata liste u zasebne promenljive za drugi pravac i
# konverzija promenljivih iz stringa u int i float za drugi pravac
stepeni2 = int(pravac2[0])
while stepeni2 in range(0, 360):
    stepeni2 = stepeni2
    break
else:
    stepeni2 = raw_input("Unesite ponovo stepene za drugi pravac ")
    stepeni2 = int(stepeni2)

minuti2 = int(pravac2[1])
while minuti2 in range(0, 60):
    minuti2 = minuti2
    break
else:
    minuti2 = raw_input("Unesite ponovo minute za drugi pravac ")
    minuti2 = int(minuti2)

sekunde2 = int(pravac2[2])
while sekunde2 in range(0, 60):
    sekunde2 = sekunde2
    break
else:
    sekunde2 = raw_input("Unesite ponovo sekunde za drugi pravac ")
    sekunde2 = int(sekunde2)


#Provera (ukloniti komentar)
# print stepeni2, minuti2, sekunde2
#Prevodjenje u decimalni zapis
dec2 = stepeni2 + minuti2/60.0 + sekunde2/3600.0
#Provera (ukloniti komentar)
# print dec2

ugao = round (dec2 - dec1, 4)

if ugao > 0:
    print  'Ugao je:' , ugao
else:
    print ugao + 360
