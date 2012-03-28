#Partie module

def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Fraction:
#    def __init__(self):
#        self.denominator = 1
#        self.numerator = 1
    
    def __init__(self, numerator = 1, denominator = 1):
        #FIXME gérer input
        if (type(numerator) != int or  type(denominator) != int ):
            raise TypeError
        self.denominator = denominator
        self.numerator = numerator
        self.simplify()
        
    def simplify(self):
        p = pgcd(self.numerator, self.denominator)
        self.numerator /= p;
        self.denominator /= p;
    
    def __add__(self, other):
        return Fraction(self.numerator * other.denominator + other.numerator + self.numerator, self.denominator * other.denominator)
    
    def __sub__(self, other):
        return Fraction(self.numerator * other.denominator + other.numerator - self.numerator, self.denominator * other.denominator)

    def __repr__(self):
        if self.denominator != 1:
            return "%d/%d" % (self.numerator, self.denominator)
        else:
            return self.numerator
    #eleg ha csak a __repr__ mar megvan
    def __str__(self):
        if self.denominator != 1:
            return "%d/%d" % (self.numerator, self.denominator)
        else:
            return str(self.numerator)

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator*other.numerator, self.denominator*other.denominator)



if __name__ == "__main__":
    #import imp
    #imp.reload(sys)
    #try:
    #f = Fraction("spaghetti",3)
    #except TypeError as e:
    #    print(e)
    f = Fraction(4,3)
    print(f)
    f = Fraction(6,4)
    print(f)
    print(-f)
    g = Fraction(4)
    print (f+g)
    print(f-g)
    print(f*g)
    #autre main
