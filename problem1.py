

def multipleOf(limit=10):
    for x in range(limit):
        if x % 3 == 0 or x % 5 == 0:
            yield x


sum = 0
for x in multipleOf(limit=1000):
    print(x)
    sum += x

print(sum)
