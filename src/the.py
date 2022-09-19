# INCOMPLETE
from logging import exception
from num import Num
from sym import Sym

class the:
    def __init__(self):
        self.eg = "nothing"
        self.dump = False
        self.file = '../data/auto93.csv'
        self.help = False
        self.nums = 512
        self.seed = 10019
        self.seperator = ","

    def get_the (self):
        return {
            "eg": self.eg,
            "dump": self.dump,
            "file": self.file,
            "help": self.help,
            "nums": self.nums,
            "seed": self.seed,
            "seperator": self.seperator
        }
        

    # Helpers
    # helper funtions need to be moved out of 'the' class
    def show (self, dict_):
        str = "{"
        for k in dict_:
            v = dict_[k]
            str += ":"
            str += k
            str += " "
            str += v.__str__()
            str += " "
        str = str[:-1] + "}"

        return str

    # −− ‘o‘: generates a string from a nested table.
    # kept only oo funtion 
    def oo (self, t):
        if type (t) != dict:
            if type (t) == Num:
                u = {}
                u['n'] = t.n
                u['at'] = t.at+1
                u['name'] = t.name
                u['lo'] = t.lo
                u['hi'] = t.hi
                u['isSorted'] = t.isSorted
                u['w'] = -1 if t.name[-1] == '-' else 1

                dict1 = dict(sorted(u.items()))
                return self.show (dict1)

            elif type (t) == Sym:
                print ('check if printing sym is needed anywhere, if so, will implement')
            return t
        else:
            # print ('the type of t is dict, this code needs to be checked')
            dict1 = dict(sorted(t.items()))
            return self.show (dict1)


        
    # def coerce (self, s):
    #     try:
    #         return int(s)
    #     except Exception as e:
    #         try:
    #             return float(s)
    #         except Exception as e:
    #             return (re.match ("^%s*(.−)%s*$", s))
