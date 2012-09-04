# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.
# -----------------------------------------------------------------------
tic

S = 0;
a = 2; b = 3;
while a <= 4000000
      S += a;
      aStep = 2*b; bStep = 2*(a'+b);  # 'simultaneous' updates
      a += aStep; b += bStep;
end
S

toc
