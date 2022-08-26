
class Fraction:
    def __init__(self,nr,dr=1):
        self.dr = dr
        self.nr = nr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1
            
    def show(self):
        print(str(self.nr) + '\\' + str(self.dr))


    def multiply(self,mcand):
        if isinstance(mcand, int):
            mcand = Fraction(mcand)
        return Fraction(self.nr*mcand.nr, self.dr*mcand.dr)

    def add(self,mcand):
        if isinstance(mcand, int):
            mcand = Fraction(mcand)
        rv = Fraction(self.nr*mcand.dr + mcand.nr*self.dr, self.dr*mcand.dr)
        return rv

f1 = Fraction(2,3)
f1.show()
f2 = Fraction(3,4)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5)
f3.show()
f3 = f1.multiply(5)
f3.show()


