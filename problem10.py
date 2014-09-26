

def sieve(limit=999999):
    h = set()
    i = 0
    for n in range(2, limit):
        if n not in h:
            i += 1
            yield n
            for x in range(n, limit, n):
                # print("x", x)
                h.add(x)

    print("has {} prime numbers".format(i))

s = sum(sieve(limit=2000000))
assert(s == 142913828922)
