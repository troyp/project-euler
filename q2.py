# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.
# -----------------------------------------------------------------------------

# simple loop + accumulator variable
S = 0
a,b = 1,2
while a<4000000:
    a,b = b,a+b
    if not a%2:
        S += a
print S

# generator soln
def fib():
    this,next = 2,3
    while this < 4000000:
        yield this
        this,next = this+2*next, 2*this+3*next
print sum(fib())

# notice that the parity of terms must proceed ...,even,odd,odd,even,...
# every third term is even: start with 2, move three steps at a time...
S = 0
a,b = 2,3
while a < 4000000:
    S += a
    a,b = a+2*b, 2*a+3*b
print S
