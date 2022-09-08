# TODO

#first change the cwd to the script path
import os, sys
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)

#append the relative location you want to import from
sys.path.append("../src")
import sym as sym_class

def test():
    # assert True

    sym_obj = sym_class.Sym ()

    for v in ["a", "a", "a", "a", "b", "b", "c"]:
        sym_obj.add (v)

    mode, entropy = sym_obj.mid(-1, -1, -1), sym_obj.div(-1, -1)
    
    # entropy = (1000*entropy)//(1/1000)
    print ("mode", mode, "entropy", entropy)

    test_result = (mode=="a" and 1.37 <= entropy and entropy <=1.38)
    print (test_result)
    
    assert test_result

test ()