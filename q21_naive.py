# Let d(n) be defined as the sum of proper divisors of n (numbers less than 
# n which divide evenly into n).
# If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
# 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are
# 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.
#---------------------------------------------------------------------------
N = 10000
total = 0

def d(n):
        if n <= 1:
                return 0
        d = 0
        for i in xrange(1, int(n/2 + 1)):
                if n%i == 0:
                        d += i
        return d
for n in xrange(1,N):
        dn = d(n)
        if d(dn) == n and dn != n:
                total += n
print total
