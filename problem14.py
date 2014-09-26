

def collatzSequence(n=13):
    while n > 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3*n + 1

        yield n


largest = 0
for i in range(13,1000000):
    s = [x for x in collatzSequence(i)]
    #print(i, len(s))
    if len(s) > largest:
        largest_i = i
        largest = len(s)

print(largest_i, largest)
assert(largest_i == 837799 and largest == 524)
