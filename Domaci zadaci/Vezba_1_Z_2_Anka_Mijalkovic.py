# Zadatak 2 (Vezba 1)

a = input("Unesi prvi ceo broj:")
b = input("Unesi drugi ceo broj:")
print a, b
help ("%")
print "Prvi broj: {0:d} \nDrugi broj: {1:d} \nZbir: {2:d} \nRazlika: {3:d} \n" \
      "Proizvod: {4:d} \nCeo deo pri deljenju prvog broja drugim brojem: {5:d} \n" \
      "Ostatak pri deljenju prvog broja drugim brojem: {6:d} \n".format(a, b, a+b, a-b, a*b, a//b ,a%b )
