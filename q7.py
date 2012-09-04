# What is the 10 001st prime number?
from itertools import count
def primes():
    yield 2
    candidates = count(3,2)
    for candidate in candidates:
        if candidate%2 == 0: continue
        n = 3
        while n*n <= candidate:
            if candidate%n == 0:
                break
            n += 2
        else:
            yield candidate

p = primes()
for i in xrange(1,10001):
    p.next()
print p.next()
