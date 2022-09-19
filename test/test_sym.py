import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'src')))
import sym as sym_class
from the import the

def test():
    sym_obj = sym_class.Sym ()

    for v in ["a", "a", "a", "a", "b", "b", "c"]:
        sym_obj.add (v)

    mode, entropy = sym_obj.mid(-1, -1, -1), round (sym_obj.div(-1, -1), 3)

    the_obj = the ()
    dict_pass = {'mid': mode, 'div': entropy}
    print (the_obj.oo(dict_pass))

    test_result = (mode=="a" and 1.37 <= entropy and entropy <=1.38)
    assert test_result

# test ()