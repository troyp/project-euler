# we move down a row each step, either left (ith->ith) or right (ith->i+1st)
# using A* with heuristic: sum the row maxima for remaining rows
# clearly, heuristic is optimistic.

datafile = open("triangle.txt")
text = datafile.readlines()
a = [[int(num) for num in line.split()] for line in text]
N = len(a)

class Path(list):
    def __init__(self, *args):
        super(Path, self).__init__(*args)
        self.val = None
    def __add__(self, other):
        res = Path(self)
        list.__iadd__(res, other)
        res.val = self.val + sum((a[i][j] for (i,j) in other))
        return res
    def __str__(self):
        return "Path: %s\nValue: %d"%(list.__str__(self), self.val)

start = Path([(0,0)])
start.val = 59

def Astar(remove_choice, actions, goal, frontier=[start], explored=[]):
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

rowmaximum = [max(row) for row in a]
def h(node):
    return sum((rowmaximum[i] for i in xrange(node[0]+1, N)))
def goal(x):   # return True if goal node
    return x[0] == N-1
def actions(x):    # return iterable containing possible next nodes
    if x[0] == N-1:
        return []
    return [(x[0]+1,x[1]), (x[0]+1,x[1]+1)]
def remove_choice(frontier):
    maxval = -1; maxpath = None
    for path in frontier:
        max_tot_path_val = path.val + h(path[-1])
        if max_tot_path_val > maxval:
            maxval = max_tot_path_val
            maxpath = path
    frontier.remove(maxpath)
    return maxpath


#print Astar(remove_choice, actions, goal)
