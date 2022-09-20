import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'src')))
from num import Num
from the import the 

def test_num():
    t = the()
    num = Num()
    for i in range(1,101):
        num.add(t, i)
    mid = num.mid()
    div = num.div()
    print(mid, div)
    assert 50 <= mid and mid <= 52 
    assert 30.5 < div and div < 32

def test_bignum():  
    t = the()
    num = Num()
    for i in range(1, 1000):
        num.add(t, i)
    print(num._has)
    assert len(num._has) == 512

test_num()
test_bignum()