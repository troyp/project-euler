# Add all the natural numbers below one thousand that are multiples of 3 or 5.
# ----------------------------------------------------------------------------
# execute within Octave session session using "source q1.m" in this dir.
# brute force: filter and sum
clear all
tic

ns = 1:999;
sum((mod(ns,3)==0 | mod(ns,5)==0) .* ns)

toc


# brute force: generate and sum
clear all
tic

n3s = 3 * (1:999/3);
n5s = 5 * (1:999/5);
ns = unique([n3s n5s]);
sum(ns)

toc


# analytic
clear all
tic

N3 = floor(999/3);
N5 = floor(999/5);
N15 = floor(999/15);
3*N3*(N3+1)/2 + 5*N5*(N5+1)/2 -15*N15*(N15+1)/2

toc
