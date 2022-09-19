import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'src')))
import the as the_class

def test():
    the_obj = the_class.the ()
    dict_pass = the_obj.get_the ()
    print (the_obj.oo(dict_pass))
    assert True

# test()