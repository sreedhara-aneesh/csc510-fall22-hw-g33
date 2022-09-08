# TODO

#first change the cwd to the script path
import os, sys
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)

#append the relative location you want to import from
sys.path.append("../src")
import sym as classs

def test():
    test_result = True
    
    assert test_result

test ()