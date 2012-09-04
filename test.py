from math import sqrt
from itertools import count
from time import time

def prime_iter():
    print "1:",
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
def prime_iter1b():
    print "1b:",
    yield 2
    candidates = count(3,2)
    for candidate in candidates:
        if candidate%2 == 0: continue
        n = 3
        while squares[n] <= candidate:
            if candidate%n == 0:
                break
            n += 2
        else:
            yield candidate

def prime_iter2():
    print "2:",
    yield 2
    candidates = count(3,2)
    for candidate in candidates:
        candidate_root = sqrt(candidate)
        if candidate%2 == 0: continue
        n = 3
        while n <= candidate_root:
            if candidate%n == 0:
                break
            n += 2
        else:
            yield candidate
squares = [i*i for i in xrange(5000000)]

t0 = time()
pi = prime_iter()
for p in pi:
        if p>5000000:
                break
print time() - t0

t0 = time()
pi = prime_iter1b()
for p in pi:
        if p>5000000:
                break
print time() - t0

t0 = time()
pi = prime_iter2()
for p in pi:
        if p>5000000:
                break
print time() - t0
