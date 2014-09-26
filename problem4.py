

def palindrome(lim=999):
    for i in range(lim, 1, -1):
        x = str(i) + str(i)[::-1]
        yield int(x)


def sieve(limit=10):
    h = set()
    for n in range(2, limit):
        if n not in h:
            yield n
            for x in range(n, limit, n):
                # print("x", x)
                h.add(x)

def factorize(n):
    factors = []
    for p in sieve(limit=100):
        if p*p > n: break
        i = 0
        while n % p == 0:
            n //= p
            i+=1
        if i > 0:
            factors.append((p, i))
    if n > 1: factors.append((n, 1))

    return factors

def divisors(factors):
    div = [1]
    for (p, r) in factors:
        div = [d * p**e for d in div for e in range(r + 1)]
    return div


def test(testn=9009, n=2):
    for x in divisors(factorize(testn)):
        if len(str(x)) == n:
            y = testn / x
            if len(str(int(y))) == n:
                print(x, y)
                return True

    return False

def run():
    lim = 999
    for x in palindrome(lim):
        if test(x, 3):
            print(x)
            break

run()