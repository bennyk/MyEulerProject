

def multipleOf(n, min, lim=999999999):
    start = n
    for x in range(min, lim):
        if x % n == 0:
            start = x
            break
    for x in range(start, lim, n):
        yield x

def run():
    prev = 1
    for p in range(2, 21):
        print(p)
        found = False
        for q in multipleOf(p, prev):
            if q % prev == 0:
                prev = q
                found = True
                break

        if not found:
            print("can't find multiple for", p)
            break

    print(prev)
    assert(232792560 == prev, "wrong answer!")

# for x in multipleOf(3):
#     print(x)

run()