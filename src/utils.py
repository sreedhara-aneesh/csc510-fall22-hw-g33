from typing import Callable
from the import the
from collections import defaultdict 

class Utils:

    def push(input_map, value):
        input_map.append(value)
        return value

    def csv(fname:str, fun:Callable):
        with open(fname, encoding="utf8") as f:
            t = {}
            for s in f.readlines():
                t = list(map(the.coerce, s.strip().split(the.seperator )))
                fun(t)
                