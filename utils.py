
def product(iterable):
	prod = 1
	for i in iterable:
		prod *= i
	return prod

# memoization decorator
def memoize(f):
	cache = {}
	def memoized(*x, **k):
		if x in cache:
			return cache[x]
		else:
			result = f(*x, **k)
			cache[x] = result
			return result
	return memoized

from itertools import count
def prime_iter():
    yield 2
    candidates = count(3,2)
    for candidate in candidates:
        if candidate%2 == 0: continue
        n = 3
        while n*n <= candidate:
            if candidate%n == 0:
                break
            n += 2
        else:
            yield candidate

def add_counts(dict1, dict2):
	result = dict1
	for key in dict2:
		result[key] = dict2[key] + dict1.get(key,0)
	return result

@memoize
def factorize_rec(n):
	if n==1:
		return {}
	"Recursive factorization function, suitable for memoization"
        for p in prime_iter():
		if p*p > n:
			return {n:1}
		if n%p == 0:
			return add_counts({p:1}, factorize_rec(n/p))

def sigma_fn(n):
        "sigma function: sum of divisors"
    fzn = factorize_rec(n)
    return product((sum((p**j for j in xrange(i+1))) for p,i in fzn.items()))
def s(n):
        "s function: aliquot sum (sum of proper divisors)"
    return sigma_fn(n) - n

def fromdigits(ds):
	return sum((d*10**n for n,d in enumerate(reversed(ds))))
		
		

def Astar(remove_choice, actions, goal, frontier, explored=[]):
    while frontier:
        #print "frontier size: %d"%len(frontier)
        path = remove_choice(frontier)
        #print "path chosen: %s"%str(path)
        s = path[-1]
        explored.append(s)
        if goal(s):
            return path
        for act in actions(s):
            result = path + [act]
            if not result[-1] in explored:
                #print "add to frontier %s"%str(result)
                #print "h(end node)=%d"%h(result[-1])
                frontier.append(result)
    else:
        return None

