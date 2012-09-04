# Find the largest prime factor of a composite number.
# ----------------------------------------------------

from math import sqrt
def factors(n):
    i = 2
    root = int(sqrt(n))
    while n > 1:
        if n%i == 0:
            yield i
            n /= i
        else:
            i += 1
            if i > root:
                yield n
                raise StopIteration
for p in factors(600851475143):
    print p,

