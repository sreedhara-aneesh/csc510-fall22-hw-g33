# row holds one record
class Row:
    def __init__(t):
        return {
            "cells": t,  # one record
            "cooked": t.copy(),  # used if we discretize data
            "isEvaled": False,  # true if y-values evaluated
        }
