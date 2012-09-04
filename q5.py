# What is the smallest positive number that is evenly divisible by all of 
# the numbers from 1 to 20?
# -----------------------------------------------------------------------
# the LCM can be calculated by multiplying all prime factors of the numbers,
# each to the highest exponent that occurs in any of the factors.

from math import sqrt
from collections import defaultdict

def factors(n):
    "returns the factorization of n as a {prime: exponent} dict."
    fz = defaultdict(int)
    while n%2 == 0:
        fz[2] += 1
        n /= 2
    i = 3
    while n > 1:
        if n%i == 0:
            fz[i] += 1
            n /= i
        else:
            i += 2
            if i*i > n:
                fz[n] = 1
                return fz
    return fz
def lcm(nums):
    lcmfz = defaultdict(int)
    for n in nums:
        fz = factors(n)
        for p in fz:
            if lcmfz[p] < fz[p]:
                lcmfz[p] = fz[p]
    lcm = 1
    for p in lcmfz:
        lcm *= p**lcmfz[p]
    return lcm

print lcm(xrange(1,21))


