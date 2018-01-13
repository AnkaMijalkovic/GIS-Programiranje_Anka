# Modul Geometrija

# Klasa Tacka
import math
import gc


class Tacka:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def koordinate(self):
        print ('({:<f}, {:<f})'.format(self.x, self.y))

    def __str__(self):
        return ' \n x = {:<f} \n y = {:<f}'.format(self.x, self.y)

    def pomeranje(self, x_pomereaj, y_pomeraj):
        x = self.x + x_pomereaj
        y = self.y + y_pomeraj
        return Tacka(x, y)

    def rastojanje(self, t):
        dx = self.x - t.x
        dy = self.y - t.y
        return math.sqrt(dx * dx + dy * dy)


# Klasa Duz
class Duz:
    def __init__(self, tp, tk):
        self.tp = Tacka(tp.x, tp.y)
        self.tk = Tacka(tk.x, tk.y)

    def __str__(self):
        return 'Pocetna tacka, tp {} \n Krajnja tacka, tk {} \n '.format(str(self.tp), str(self.tk))

    def kreiraj_duz(self, xp, yp, xk, yk):
        tp = Tacka(xp, yp)
        tk = Tacka(xk, yk)
        d = Duz(tp, tk)
        return d

    def duzina(self):
        return self.tp.rastojanje(self.tk)


