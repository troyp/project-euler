#   Starting with the number 1 and moving to the right in a clockwise direction
#   a 5 by 5 spiral is formed as follows:
#   
#   21 22 23 24 25
#   20  7  8  9 10
#   19  6  1  2 11
#   18  5  4  3 12
#   17 16 15 14 13
#   
#   It can be verified that the sum of the numbers on the diagonals is 101.
#   
#   What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
#   formed
#   in the same way?
# -----------------------------------------------------------------------------

# for an n x n square:
# The top right corner has the greatest number, n*n.
# Each successive corner working acc is (n-1) less
# The sum of these 4 corners is 4n^2 - 6(n-1)  where n>1

# Now we want to sum the corners for squares n=3,5,7,... (and add the middle 1)
# Say we have a square spiral of size N x N and let K = (N-1)/2
# K will be the number of individual squares (not counting the centre 1)
# Summing -6(n-1) for n=3,5,7,...,N
#   gives -6(2+4+6+...) = -12(1+2+3+...) = -6K(K+1)
# Now summing 4n^2 gives 4(9+25+49+...)
#   The series 1+9+25+...+n^3 is a cubic polynomial with constant term 0
#   setting an^3 + bn^2 +cn = 1+9+25+...+n^2, we set n=1,2,3 and solve
#   to get sum = (4/3)(K+1)^3 - (1/3)(K+1)
#   or 9+25+...+n^2 = (4/3)(K+1)^3 - (1/3)(K+1) - 1
#   So the 4n^2 terms sum to (16/3)(K+1)^3 - (4/3)(K+1) - 4
# So our total sum is (16/3)(K+1)^3 - (4/3)(K+1) - 4 - 6K(K+1) + 1
#   or (16/3)K^3 + 10K^2 + (26/3)K + 1

def sum_diags(N):
    K = (N-1)/2
    return (16*K**3 + 30*K**2 + 26*K + 3)/3
print sum_diags(1001)
