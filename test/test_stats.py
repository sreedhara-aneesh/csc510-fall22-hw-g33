# first change the cwd to the script path
import string
from data_class import Data
from sym import Sym
from num import Num
import os
import sys
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)

# append the relative location you want to import from
sys.path.append("../src")

# print some stats on columns


def test():
    data = Data('../src/data/auto93.csv')

    def div(col):
        return col.div()

    def mid(col):
        return col.mid()

    def oo(self, t):
        if type(t) != dict:
            if type(t) == Num:
                u = {}
                u['n'] = t.n
                u['at'] = t.at+1
                u['name'] = t.name
                u['lo'] = t.lo
                u['hi'] = t.hi
                u['isSorted'] = t.isSorted
                u['w'] = -1 if t.name[-1] == '-' else 1

                dict1 = dict(sorted(u.items()))
                return self.show(dict1)

            elif type(t) == Sym:
                print('check if printing sym is needed anywhere, if so, will implement')

            elif type(t) == list:
                return self.show(t)
            # return t

        else:
            # print ('the type of t is dict, this code needs to be checked')
            dict1 = dict(sorted(t.items()))
            return self.show(dict1)
    print("xmid", oo(data.stats(2, data.cols.x, mid)))
    print("xdiv", oo(data.stats(3, data.cols.x, div)))
    print("ymid", oo(data.stats(2, data.cols.y, mid)))
    print("ydiv", oo(data.stats(3, data.cols.y, div)))
    assert True


def test():
    assert True
