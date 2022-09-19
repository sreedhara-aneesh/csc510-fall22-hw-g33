import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'src')))
from num import Num
from row import Row # TODO use Row class from other commit 
from the import the
from utils import Utils



def checkcsv(n):
    test_result = True
    global rows
    rows = rows + 1
    if rows> 10:
        return
    else:
        the.oo(n)
    assert test_result

def test_csv():
    csv_filename = "./data/auto93.csv"
    Utils.csv(csv_filename, checkcsv)

def test():
    global rows
    rows = 0
    test_csv()

# test()