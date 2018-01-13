# Zadatak 7 (Vezba 1)

x1 = input('Unesite x koordinatu prvog temena tacke A')
y1 = input('Unesite y koordinatu prvog temena tacke A')

x2 = input('Unesite x koordinatu drugog temena tacke B')
y2 = input('Unesite y koordinatu drugog temena tacke B')

x3 = input('Unesite x koordinatu treceg temena tacke C')
y3 = input('Unesite y koordinatu treceg temena tacke C')

xm = input('Unesite x koordinatu ispitivane tacke M')
ym = input('Unesite y koordinatu ispitivane tacke M')

p = 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) #povrsina trougla 123

p1 = 0.5 * abs(x2*(ym-y3) + xm*(y3-y2) + x3*(y2-ym))  #povrsina trougla M23
p2 = 0.5 * abs(x1*(ym-y3) + xm*(y3-y1) + x3*(y1-ym))  #povrsina trougla M13
p3 = 0.5 * abs(x1*(y2-ym) + x2*(ym-y1) + xm*(y1-y2))  #povrsina trougla M12

sumap = p1 + p2 + p3 #Suma trouglova
   #da bi tacka M pripadala trouglu 123, suma povrsina trouglova M12, M23 i M13 treba biti ista kao povrsina trougla 123
if sumap==p:
    print 'DA'
else:
    print 'NE'