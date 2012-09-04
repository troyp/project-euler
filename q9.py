# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# ------------------------------------------------------------------------
# We have [1] a+b+c=1000, [2] a^2+b^2=c^2
# Squaring and expanding [1]: a^2 + b^2 + c^2 + 2(ab+bc+ac) = 10^6
# Substituting using [2]:     2c^2 + 2(ab+bc+ac) = 10^6
# factorizing:                2(a+c)(b+c) = 10^6
# substituting using [1]:     2(a+c)(1000-a) = 10^6
# So we want a solution to (a+c)(1000-a) = 500000

# a,c are in N so we know a+c > 500
# also c>=5 (first pythagorean triple RHS)
def main():
        for a in xrange(1,995):
                for c in xrange(501-a, 1000-a):
                        if (a+c)*(1000-a) == 500000:
                                return a*(1000-a-c)*c
print main()
