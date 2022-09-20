from logging import exception
from num import Num
from sym import Sym

# -- Parse ‘the‘ config settings from ‘help‘.
help= """
−e −−eg start−up example = nothing
−d −−dump on test failure, exit with stack dump = false
−f −−file file with csv data = ./data/auto93.csv
−h −−help show help = false
−n −−nums number of nums to keep = 512
−s −−seed random number seed = 10019
−S −−seperator feild seperator = ,"""

class the:
    eg = "nothing"
    dump = False
    filename = './data/auto93.csv'
    help = False
    nums = 512
    seed = 10019
    seperator = ","
    
    def __init__(self):
        self.eg = "nothing"
        self.dump = False
        self.filename = './data/auto93.csv'
        self.help = False
        self.nums = 512
        self.seed = 10019
        self.seperator = ","

    # def get_the(self):
    #     return (
    #         "−e −−eg start−up example = " + str (self.eg) + "\n" +
    #         "−d −−dump on test failure, exit with stack dump = " + str (self.dump) + "\n" +
    #         "−f −−file file with csv data = " + str (self.filename) + "\n" +
    #         "−h −−help show help = " + str (self.help) + "\n" +
    #         "−n −−nums number of nums to keep = " + str (self.nums) + "\n" +
    #         "−s −−seed random number seed = " + str (self.seed) + "\n" +
    #         "−S −−seperator feild seperator = " + str (self.seperator) + "\n" +
    #         "−1 −−exit terminate program\n"
    #     )
    def get_the(self):
        return_the_dict = {
            "eg":self.eg,
            "dump":self.dump,
            "filename":self.filename,
            "help":self.help,
            "nums":self.nums,
            "seed":self.seed,
            "seperator":self.seperator
        }
        return return_the_dict

    # Helpers
    # helper funtions need to be moved out of 'the' class
    def show(self, dict_):
        str = "{"
        if type (dict_) == dict:
            for k in dict_:
                v = dict_[k]
                str += ":"
                str += k
                str += " "
                str += v.__str__()
                str += " "
            str = str[:-1] + "}"
        else:
            for k in dict_:
                str += k.__str__()
                str += " "
                
            str = str[:-1] + "}"

        return str

    # −− ‘o‘: generates a string from a nested table.
    # kept only oo funtion 
    # def oo (t):
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
                return self.show(dict1)

            elif type (t) == Sym:
                print ('check if printing sym is needed anywhere, if so, will implement')

            elif type (t) == list:
                return self.show(t)
            # return t

        else:
            # print ('the type of t is dict, this code needs to be checked')
            dict1 = dict(sorted(t.items()))
            return self.show(dict1)

    # −− Update settings from values on command−line flags. Booleans need no values
    # −− (we just flip the defaults).
    def CLI (self):
        # input
        while True:
            print (self.get_the ())
            input1 = input ()
            inputs = input1.split (" ")
            if inputs[0] == '-h':
                i = 0
            elif inputs[0] == '-e':
                # TODO
                print ('yet to implement\n')
            elif inputs[0] == '-d':
                self.dump = (self.dump == False) or False
            elif inputs[0] == '-f':
                self.filename = inputs[1]
            elif inputs[0] == '-n':
                self.nums = inputs[1]
            elif inputs[0] == '-s':
                self.seed = inputs[1]
            elif inputs[0] == '-S':
                self.seperator = inputs[1]
            elif inputs[0] == '-1':
                print ("Terminating program..")
                exit (0)
        
    def coerce(s:str):
        try:
            return int(s)
        except Exception as e:
            try:
                return float(s)
            except Exception as e:
                return s

# t = the ()
# t.CLI ()