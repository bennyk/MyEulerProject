import math

def distance(a, b):
    return math.sqrt(a ** 2 + b ** 2)

class Fraction:

    def __init__(self, term, numer, denom):
        self.term = term
        self.numer = numer
        self.denom = denom

    def convertToImproper(self):
        return Fraction(1, self.denom * self.term + self.numer, self.denom)

    def __str__(self):
        if self.term == 1:
            return "{}/{}".format(self.numer, self.denom)
        else:
            return "{} {}/{}".format(self.term, self.numer, self.denom)

    def pyTriplet(self):
        improper = self.convertToImproper()
        return (improper.denom, improper.numer, distance(improper.numer, improper.denom))


# for odd-odd pairs use m=3, n=1
def genCoPrime(m=2, n=1, limit=500):
    yield (m, n)
    if m < limit and n < limit:
        yield from genCoPrime(2*m - n, m)
        yield from genCoPrime(2*m + n, m)
        yield from genCoPrime(m + 2*n, n)


def genStifelNumbers(lim=100):
    adj = 1
    for x in range(1, lim+1):
        adj += 1
        f = Fraction(x, x, x+adj)
        t = f.pyTriplet()
        print(f, f.convertToImproper(), f.pyTriplet(), sum(t))
        if sum(t) == 1000 or 1000 % sum(t) == 0:
            print("got it", f.pyTriplet())
            break

#genStifelNumbers()

def farey( n, asc=True ):
    """Python function to print the nth Farey sequence, either ascending or descending."""
    if asc:
        a, b, c, d = 0, 1,  1  , n     # (*)
    else:
        a, b, c, d = 1, 1, n-1 , n     # (*)
    # print("%d/%d" % (a,b))
    yield (a, b)
    while (asc and c <= n) or (not asc and a > 0):
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
        # print("%d/%d" % (a,b))
        yield (a, b)

def testEuler():
    for n, m in farey(10000):
        if m > n and (m-n) % 2 != 0:
            z = m**2 + m*n
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            print(m, n, '-', a, b, c, a + b + c)

            if (a + b + c) == 1000:
                print(m, n)
                break

def testCoprime():
    for x in farey(100):
        if x == (2, 9):
            print('got it')
            break
        print(x)


def testDickson():
    for s, t in genCoPrime():
        if s == 0 or t == 0:
            continue

        r = math.sqrt(2*s*t)
        if (r - int(r)) == 0.0:
            r = int(r)
            x = r + s
            y = r + t
            z = r + s + t
            zz = x + y + z
            # print(s, t, r, x, y, z, zz)
            if zz == 1000 or 1000 % zz == 0:
                print('got it')
                k = 1000/zz
                print(r, s, t, ':', x, y, z, ':', x*k, y*k, z*k, zz)

                # answer
                assert(31875000 == x * y * z * k ** 3)

# testEuler()
# testCoprime()
testDickson()
