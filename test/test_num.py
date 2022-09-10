import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'src')))
from num import Num

def test_num():
    
    # TODO: replace with actual The class after it is implemented
    class MockThe:
        def __init__(self):
            self.nums = 100
    the = MockThe()

    num = Num(the)
    for i in range(1,101):
        num.add(the, i)
    mid = num.mid()
    div = num.div()
    assert 50 <= mid and mid <= 52 
    assert 30.5 < div and div < 32

def test_bignum():
    
    # TODO: replace with actual The class after it is implemented
    class MockThe:
        def __init__(self):
            self.nums = 32
    the = MockThe()

    num = Num(the)
    for i in range(1, 1001):
        num.add(the, i)
    assert len(num._has) == 32