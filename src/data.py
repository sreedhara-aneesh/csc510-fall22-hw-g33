# INCOMPLETE

# -- ‘Data‘ is a holder of ‘rows‘ and their sumamries (in ‘cols‘).

# TODO: replace with actual The class after it is implemented
class MockCols:
    def __init__(self, names):
        self.names=names #−− all column names
        self.all={} #−− all the columns (including the skipped ones)
        self.klass=None #−− the single dependent klass column (if it exists)
        self.x={} #−− independent columns (that are not skipped)
        self.y={} #−− depedent columns (that are not skipped)

    def add (self, item):
        return True


class Data:
    def __init__(self, src):
        self.cols = None # summaries of data
        self.rows = {} # kept data
        # TODO
       
    # −− Add a ‘row‘ to ‘data‘. Calls ‘add()‘ to update the ‘cols‘ with new values.
    # INCOMPLETE
    def add (self, xs):
        if self.cols == None:
            self.cols = MockCols (xs)
        else:
            row = self.rows + (xs.cells) + xs #TODO
            for _, todo in (self.cols.x, self.cols.y):
                for _,col in (todo):
                    col.add (row.cells[col.at])

    #−− For ‘showCols‘ (default=‘data.cols.x‘) in ‘data‘, show ‘fun‘ (default=‘mid‘),
    #−− rounding numbers to ‘places‘ (default=2)
    def stats(self, showCols, fun, v):
        places = 2
        showCols, fun = showCols or self.cols.y, fun or "mid"
        t={}; 
        for _,col in showCols:
            v =fun(col)
            v=type(v)=="number" and round(v, places)
            t[col.name]=v
        return t


