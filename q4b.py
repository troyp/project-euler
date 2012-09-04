# Find the largest palindrome made from the product of two 3-digit numbers.
# -------------------------------------------------------------------------

# Note: palindrome must be in range [10000, 998001]
# We have either:
#  - a 6-digit palindrome defined by first 3 digits in range [100, 997]; or
#  - a 5-digit palindrome defined by first 3 digits in range [100, 999]
seeds6 = xrange(997,99,-1)
seeds5 = xrange(999,99,-1)
def palindromes_in_range():
    for seed in seeds6:
        yield palindrome6(seed)
    for seed in seeds5:
        yield palindrome5(seed)
def main():
    for candidate in palindromes_in_range():
        for factor in xrange(max(100, candidate/999),
                             min(1000, candidate/100 + 1)):
            if candidate%factor == 0:
                return candidate

def rdigits(n):
    "returns list of digits of an integer in reverse order"
    ds = []
    while n:
        d = n%10
        ds.append(d)
        n /= 10
    return ds
def fromdigits(ds):
    "returns integer given list of digits"
    n = 0
    for d in ds:
        n = 10*n + d
    return n
def palindrome6(n):
    "returns 6-digit palindrome given 3-digit integer"
    for d in rdigits(n):
        n = n*10 + d
    return n
def palindrome5(n):
    "returns 5-digit palindrome given 3-digit integer"
    for d in rdigits(n)[1:]:
        n = n*10 + d
    return n

print main()
