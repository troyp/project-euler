# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.
# ---------------------------------------------------------------------------
# The square of sums, SSQ = 1*1+2*2+...+100*100
# The square of the sum is (1+2+...+100)(1+2+...+100) = the sum of products
# i*j where i and j each take every possible value from 1 to 100.
# ie. 1*1+1*2+...+1*100 + 2*1+2*2+...+2*100 + ... + 100*1+100*2+...+100*100
# Note that every product of two factors will occur twice (once in each of
# two orders), except when the two factors are equal (ie. the squares).
# So we can write SQS = SSQ + 2*sum(i*j |i<j)

# Thus SQS-SSQ = 2*sum(i*j | i<j)
# Note that the terms to be summed are the 2-combinations without repetition
# of the numbers {1,..,100}
from math import factorial
from itertools import combinations, imap
from utils import memoize

print 2*sum(imap(lambda (i,j): i*j,
                 combinations(xrange(1,101), 2)))


# analytic formula using Faulhaber's formula
# sum[1 to n]{i**m} = (1/(m+1)) * sum[k=0 to m]{C(m+1, k) * B(k) * n**(m+1-k)}
# where C(m+1,k)=# combs of k from m+1, B(k)=kth Bernoulli No.
# so SSQ = 1/3 * sum[k=0 to 2]{C(3,k) * B(k) * n**(3-k)}
#    SQS = (.5*100*101)**2

@memoize
def Bernoulli(m):
        if m==0: return 1
        if m%2 and m>1: return 0
        return -1 * sum([C(m,k)*Bernoulli(k)/(m-k+1.0) for k in range(0,m)])

def C(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

SQS = (100*101/2)**2
SSQ = int(sum([C(3,k)*Bernoulli(k)*100**(3-k) for k in range(0,3)]))/3
print SQS - SSQ


# Using the special case of Faulhaber's formula for square pyramidal numbers
def triangular(n): return n*(n+1)/2
def square_pyramidal(n): return (2*n**3 + 3*n**2 + n)/6
print triangular(100)**2 - square_pyramidal(100)
