# Zadatak 6 (Vezba 2)
import numpy as np
import matplotlib.pyplot as plt

br_tacaka = input('Unesite zeljeni broj tacaka kroz koje se provlaci polinom')
i = 0
x = []
y = []
while i < br_tacaka:
    x.append(input('unesite x'))
    y.append(input('unesite y'))
    i = i+1
stepen_poli = input('Unesite stepen polinoma')
coefs1 = np.polyfit(x, y, stepen_poli)    # np.polyfit returns: ... + Ax^2 + Bx + C
ffit1 = np.poly1d(coefs1)
#print coefs1
print ffit1

x_new = np.linspace(x[0], x[-1], num=len(x)*10)
ffitf = np.poly1d(coefs1)    # instead of np.poly1d
plt.plot(x_new, ffitf(x_new))


#coefs2 = np.polynomial.polynomial.polyfit(x, y, stepen_poli)  # returns coefficients [A, B, C] to A + Bx + Cx^2 + ...
#ffit2 = np.poly1d(coefs2)
#print coefs2
#print ffit2
