import os
from cols import Cols
from row import Row
from num import Num
from sym import Sym
from the import the

class Data:
    def __init__(self, src):
        self.cols = None
        self.rows = []

        # src is path of a csv file
        if os.path.exists(os.path.dirname(src)):
            # you have to read the csv file here

            with open(src) as f:
                i = 0
                for line in f.readlines():
                    # print(line) # values for one row
                    line = line.replace ("\n", "")
                    # print (i)
                    i += 1
                    
                    # split the values by comma
                    values = line.split (',')

                    self.add (values)

        # src is string -> row/rows
        else:
            '''
            this a row or few rows of the csv
            for example, single row: "'1', '5', 'A', '0'" # assuming that, this string is not splitted
            multi rows: list of "'1', '5', 'A', '0'"
            '''
            
            if len (src) == 1:
                # split the values by comma
                values = src.split (',')
                self.add (values)
            else:
                for row in src:
                    # split the values by comma
                    values = row.split (',')
                    self.add (values)

    def add (self, values):
        t = the ()

        if self.cols == None: 
            # while reading the csv first time, create the cols from csv header 
            self.cols = Cols (values)
        else: 
            '''
            csv header already exists, add (row_at, col_at) entry
            create a row object
            '''
           
            row = Row (values)
            self.rows.append (row)

            # update x and y cols
            dict_x = self.cols.x # list of x col names
            dict_y = self.cols.y # list of y col names

            # from the values list, find in which x col, you can insert a specific value
            for index in dict_x: 
                col = dict_x[index]
                if isinstance(col, Sym):
                    col.add (values [col.at])
                elif isinstance(col, Num):
                    col.add (t, values [col.at])

            # from the values list, find in which y col, you can insert a specific value
            for index in dict_y: 
                col = dict_y[index]
                if isinstance(col, Sym):
                    col.add (values [col.at])
                elif isinstance(col, Num):
                    col.add (t, values [col.at])

    # −− For ‘showCols‘ (default=‘data.cols.x‘) in ‘data‘, show ‘fun‘ (default=‘mid‘),
    # −− rounding numbers to ‘places‘ (default=2)

    def stats (self, places, showCols, fun):
        if showCols == None:
            showCols = self.cols.y
        
        if places == None:
            places = 2

        table = {}

        for index in showCols:
            col = showCols[index]
            if fun == None:
                v = col.mid ()
            else:
                v = col.fun # check: call function for Num/Sym that is passed as a parameter

            if type (v) == float:
                v = round (v, places)
            table [col.name]=v

        print (table)

    def print_rows (self):
        for row in self.rows:
            print (row.get_row ())

    def print_cols (self):
        self.cols.print_()

