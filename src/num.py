import math
import random

# -- Num summarizes a stream of numbers.


class Num:

    def __init__(self, c=0, s=""):
        self.n = 0  # items seen
        self.at = c  # column position
        self.name = s  # column name
        self._has = {}  # kept data
        self.lo = float('inf')  # lowest seen
        self.hi = float('-inf')  # highest seen
        self.isSorted = True  # no updates since last sort of data

    # return the 'p'-th thing from the sorted list 't'
    def per(t, p=.5):
        p = math.floor((p*len(t)) + .5)
        return t[max(1, min(len(t), p))]

    # Return kept numbers, sorted
    def nums(self):
        if not self.isSorted:
            self._has = sorted(self._has)
            self.isSorted = True
        return self._has

    # Reservoir sampler. Keep at most 'the.nums' numbers
    # (and if we run out of room, delete something old, at random).,
    def add(self, the, v):
        if v != "?":
            self.n = self.n + 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            if (len(self._has) < the.nums):
                pos = 1 + len(self._has)
            elif (random.random() < (the.nums / self.n)):
                pos = random.random() * len(self._has)
            if (pos):
                self.isSorted = False
                self._has[pos] = int(v)

    # Diversity (standard deviation for Nums, entropy for Syms)
    def div(self):
        a = self.nums()
        return (self.per(a, .9)-self.per(a, .1)) / 2.58

    # Central tendancy (median for Nums, mode for Syms)
    def mid(self):
        return self.per(self.nums(), .5)
