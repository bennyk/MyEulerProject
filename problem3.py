

def sieve(limit=10):
    h = set()
    for n in range(2, limit):
        if n not in h:
            yield n
            for x in range(n, limit, n):
                # print("x", x)
                h.add(x)

sum = 1
# testn = 13195
testn = 600851475143
for x in sieve(10000):
    if testn % x == 0:
        sum *= x
        print(x, sum)
        if sum >= testn:
            print("largest prime is", x)
            break

