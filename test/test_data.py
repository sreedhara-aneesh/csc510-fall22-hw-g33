# INCOMPLETE

#first change the cwd to the script path
import os, sys
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)

#append the relative location you want to import from
sys.path.append("../src")
import data as data_class
import the as the_class

def test():
    csv_filename = "auto93.csv"
    data_obj = data_class.Data (csv_filename)

    the_object = the_class.the ()
         
    for _,col in (data_obj.cols.y):
        the_object.oo(col)
    
    test_result = True
    assert test_result

# test ()