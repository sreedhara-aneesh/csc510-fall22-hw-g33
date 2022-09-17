import math
import random

# -- Num summarizes a stream of numbers.


class Num:

    def __init__(self, c=0, s=""):
        self.n = 0  # items seen
        self.at = c  # column position
        self.name = s  # column name
        self._has = []  # kept data
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
        v = float (v) #tithi
        if v != "?":
            self.n = self.n + 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            if (len(self._has) < the.nums):
                pos = len(self._has)
                self._has.append(int(v))
                self.isSorted = False
            elif (random.random() < (the.nums / self.n)):
                pos = math.floor(random.random() * len(self._has))
                self._has[pos] = int(v)
                self.isSorted = False

    # Diversity (standard deviation for Nums, entropy for Syms)
    def div(self):
        a = self.nums()
        return (Num.per(a, .9)-Num.per(a, .1)) / 2.58

    # Central tendancy (median for Nums, mode for Syms)
    def mid(self):
        return Num.per(self.nums(), .5)
