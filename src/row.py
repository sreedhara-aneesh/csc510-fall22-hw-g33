# row holds one record
class Row:
    # def __init__(t):
    #     return {
    #         "cells": t,  # one record
    #         "cooked": t.copy(),  # used if we discretize data
    #         "isEvaled": False,  # true if y-values evaluated
    #     }

    def __init__(self, t): #tithi
        self.cells = t  # one record
        self.cooked = t.copy()  # used if we discretize data
        self.isEvaled = False  # true if y-values evaluated
    
    def get_row (self): #tithi
        return {
            "cells": self.cells,  # one record
            "cooked": self.cooked,  # used if we discretize data
            "isEvaled": self.isEvaled,  # true if y-values evaluated
        } 
