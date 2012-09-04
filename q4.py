# Find the largest palindrome made from the product of two 3-digit numbers.
# -------------------------------------------------------------------------

# factorizing 111111 gives 3*7*11*13*37=231*481, so a 6-digit soln exists
# Thus, we need only consider length-6 palindromes
# palindrome must be in range [100000, 998001] and
# 3-digit factor must be in range [101,999]

def palindromes_in_range():
    for seed in xrange(997,100,-1):
        yield palindrome6(seed)
def palindrome6(n):
    "returns 6-digit palindrome given 3-digit 'seed' integer"
    res = n
    while n:
        res = 10*res + n%10
        n /= 10
    return res
def main():
    for candidate in palindromes_in_range():
        for factor in xrange(max(101, candidate/999),
                             min(1000, candidate/100 + 1)):
            if candidate%factor == 0:
                assert 100 <= candidate/factor <= 999
                return candidate
print main()
