

def sieve(k, limit=999999):
    h = set()
    i = 0
    for n in range(2, limit):
        if n not in h:
            i += 1
            if k == i:
                return n
            for x in range(n, limit, n):
                # print("x", x)
                h.add(x)

    print("has {} prime numbers".format(i))

assert(sieve(10001) == 104743)
