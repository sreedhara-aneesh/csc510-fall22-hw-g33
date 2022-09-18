import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'src')))
from data_class import Data
from the import the

def test():
    csv_filename = "../data/auto93.csv"
    data_obj = Data (csv_filename)

    t = the ()
    dict_y = data_obj.cols.y
    for index in dict_y: # from the values list, find in which y col, you can insert a specific value
        col = dict_y[index]
        print (t.oo (col))

    assert True
    

# test () 
# 
# 
