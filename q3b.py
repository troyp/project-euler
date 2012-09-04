# Find the largest prime factor of a composite number.
# ----------------------------------------------------
# some optimization

from math import sqrt
def factors(n):
    while n%2 == 0:
        yield 2
        n /= 2
    i = 3
    while n > 1:
        if n%i == 0:
            yield i
            n /= i
        else:
            i += 2
            if i*i > n:
                yield n
                raise StopIteration

for p in factors(600851475143): pass
print p
