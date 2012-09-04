# Find the sum of all the primes below two million.
# -------------------------------------------------
# using constant space trial-division algorithm from q7.py

from itertools import count, takewhile
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

ps = primes()
print sum(takewhile(lambda p: p<2000000, ps))
