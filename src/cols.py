from num import Num
from sym import Sym
from utils import Utils

# ‘Columns‘ Holds of summaries of columns.
# Columns are created once, then may appear in multiple slots.
class Cols:
    names = list(str())
    all = []
    klass = None
    x = []
    y = []
    def __init__(self, names):
        self.names = names  # all column names
        self.all = []  # all the columns (including the skipped ones)
        self.klass = None  # the single dependent klass column (if it exists)
        self.x = []  # independent columns (that are not skipped)
        self.y = []  # depedent columns (that are not skipped)
        for index, value in enumerate(names):
            # Numerics start with Uppercase
            print(value[0])
            if value[0].isalpha() and value[0].isupper():
                col = Num(index, value) 
            else:
                col = Sym(index, value)
            Utils.push(self.all, col)
            endVal = self.all[-1]
            if not value.endswith(':'):  # columns ending with ':' are skipped
                if any(value.endswith(i) for i in ['+', '!', '-']):
                    Utils.push(self.y, endVal) 
                else:
                    Utils.push(self.x, endVal)
            if value.endswith('!'):
                self.klass = col

    def print_ (self):
        print (self.names)
        # print (self.all)
        # print (self.klass)
        # print (self.x)
        # print (self.y)
    