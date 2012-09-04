# Find the sum of all the primes below two million.
# -------------------------------------------------
# using prime sieve

from bitarray import bitarray
isprime = bitarray(2000000)
isprime.setall(True)
isprime[:2] = False
isprime[4::2] = False
isprime[6::3] = False
isprime[10::5] = False

n = 7
while n < 2000000 - 6:
    if isprime[n]:
	isprime[n*n::n] = False
    if isprime[n+4]:
	isprime[(n+4)*(n+4)::n+4] = False
    n += 6

print sum([n for n in xrange(2000000) if isprime[n]])
