
import math
import garbage
import gc

class Sfera:
    broj = 0  #klasna promenljiva koja broji objekte klase
    def __init__(self, r=1, x=0, y=0, z=0):
        self.r = r
        self.x = x
        self.y = y
        self.z = z
        Sfera.broj += 1   #povecava klasnu promenljivu za 1
    @staticmethod
    def broj_sfera():   # vraca ukupan broj objekata
        return Sfera.broj
        #print 'Broj Sfera jednak je: {0:d}' .format(Sfera.broj)
    def zapremina(self):
        return (4/3)*self.r*self.r*self.r*math.pi

    #def brisanje(self): # ne funkcionise.....
    #    delete itself
    #def __del__(self):
    #    print 'brise instance klase'


#print Sfera.broj_sfera()
#s1 = Sfera(4,1,2,5)
#s2 = Sfera (5,5,6,9)
#s3 = Sfera(5,4,7,8)
#print s1.broj_sfera()
#br_sf = s1.broj_sfera()
#print br_sf
#print s1.zapremina()

#print Sfera.broj_sfera()

#lista_svih_sfera = []
#for obj in gc.get_objects():
#    if isinstance(obj, Sfera):
#        lista_svih_sfera.append(obj)
##print lista_svih_sfera
#
#lista_zapremina = []
#for i in lista_svih_sfera:
#    lista_zapremina.append(i.zapremina())
#print lista_zapremina
#


