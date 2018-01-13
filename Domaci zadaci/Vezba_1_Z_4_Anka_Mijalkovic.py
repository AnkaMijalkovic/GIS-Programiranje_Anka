# Zadatak 4 (Vezba 1)

broj1 = raw_input('Unesite prvi cetvorocifreni broj')
while len(broj1)!=4:
    broj1 = raw_input('Unesite ponovo prvi cetvorocifreni broj')

broj2 = raw_input('Unesite drugi cetvorocifreni broj')
while len(broj2)!=4:
    broj2 = raw_input('Unesite ponovo drugi cetvorocifreni broj')

#Suma cifara drugog broja
sum = 0
for i in broj2:
    sum = sum + int(i)
print 'Suma cifara drugog broja je' , sum

#razlika zbira parnih od neparnih
sumpar = 0
sumnep = 0
for i in broj1:
    if int(i)%2==0:
        sumpar += int(i)
    else:
        sumnep += int(i)
print 'Razlika zbira parnih cifara i zbira neparnih cifara' , sumpar-sumnep

#
#parpoz = 0
#neppoz = 0
#for i in broj1:
 #   if broj1.index(i)  % 2 == 0:
#        parpoz += int(i)
#print parpoz

#Razlika suma cifara na parnim i neparnim pozicijama
razlika = int(broj1[0]) + int(broj1[2]) - int(broj1[1]) - int(broj1[3])
print 'Razlika suma cifara na parnim i neparnim pozicijama', razlika
