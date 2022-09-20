import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'src')))
import string
from dataclass import Data
from sym import Sym
from num import Num
from the import the
# import os
# import sys
# scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
# os.chdir(scriptPath)

# append the relative location you want to import from
# sys.path.append("../src")

# print some stats on columns

def div(col):
        return col.div()

def mid(col):
    return col.mid()

def oo(t):
    to = the()
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
            return to.show(dict1)

        elif type(t) == Sym:
            print('check if printing sym is needed anywhere, if so, will implement')

        elif type(t) == list:
            return to.show(t)
        # return t

    else:
        # print ('the type of t is dict, this code needs to be checked')
        dict1 = dict(sorted(t.items()))
        return to.show(dict1)

def test():
    t = the()
    data = Data(t.filename)
    print("xmid", oo(data.stats(2, data.cols.x, mid)))
    print("xdiv", oo(data.stats(3, data.cols.x, div)))
    print("ymid", oo(data.stats(2, data.cols.y, mid)))
    print("ydiv", oo(data.stats(3, data.cols.y, div)))
    assert True


# def test():
#     assert True

# test()