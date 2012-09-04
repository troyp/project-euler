# What is the value of the first triangle number to have over 
# five hundred divisors?
# -----------------------------------------------------------

# if n = a1*p1 + a2*p2 + ..., then num_divisors(n) = (a1+1)(a2+1)...
# since each prime factor pk may occur 0 to ak times in a factor
# We can see that num_div(n1*n2) = num_div(n1) * num_div(n2)
# when n1,n2 are coprime

# a triangle number 1+...+n has the form (1/2)*n*(n+1)
# by halving n when odd or (n+1) when even, we can write the sequence
# [ i(2i-1), i(2i+1) for i=1,2,3,... ]
from itertools import count

FZS = [ None, {}, {2:1}, {3:1}, {2:2}, {5:1} ]

def d(n):
    prod = 1
    for p in FZS[n]:
        prod *= FZS[n][p]+1
    return prod

# note: factorize must be executed on integers in ascending order
def factorize(n, cache=FZS):    #cache is a sequence of dicts
    if len(cache) > n:
        return cache[n]
    else:
        i = 2
        while i*i <= n:
            if n%i == 0:
                result = cache[n/i].copy()
                result[i] = 1 + result.get(i, 0)
                cache.append(result)
                return(result)
            i += 1
        else:
            cache.append({n:1})
            return {n:1}

for i in count(1):
    for n in xrange(len(FZS), 2*i+2):
        factorize(n)
    d_i = d(i)
    d1 = d_i * d(2*i-1)
    if d1 > 500:
        print i*(2*i-1)
        break
    d2 = d_i * d(2*i+1)
    if d2 > 500:
        print i*(2*i+1)
        break
