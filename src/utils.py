from typing import Callable
from the import the


class Utils:

    def push(input_map, value):
        current_length = len(input_map)
        input_map[current_length+1] = value
        return value

    def csv(fname:str, fun:Callable):
        with open(fname, encoding="utf8") as f:
            t = {}
            for s in f.readlines():
                t = list(map(the.coerce, s.strip().split(the.seperator )))
                fun(t)
                