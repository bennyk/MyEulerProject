
n = 100
s = sum(range(n + 1))
s **= 2

for x in range(n + 1):
    s -= x ** 2

print(s)
