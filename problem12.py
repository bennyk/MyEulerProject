

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


def triangularNumber(lim=999):
    s = 0
    for i in range(1, lim + 1):
       s += i
       yield s


for x in triangularNumber(lim=99999):
    # print(x, divisors(factorize(x)))
    divs = divisors(factorize(x))
    if len(divs) > 500:
        print(x, divs)
        break


