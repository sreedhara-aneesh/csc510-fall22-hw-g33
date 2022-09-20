import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'src')))
from num import Num
from row import Row # TODO use Row class from other commit 
from utils import Utils
import the as the_class

def checkcsv(n):
    test_result = True
    global rows
    rows = rows + 1
    if rows> 10:
        return
    else:
        the_obj = the_class.the ()
        print (the_obj.oo(n))
    assert test_result

def test():
    global rows
    rows = 0
    the_obj = the_class.the ()
    csv_filename = the_obj.filename
    Utils.csv(csv_filename, checkcsv)

# test()