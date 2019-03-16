#make sure thinhs are declared before used
#line after delcares locations
#no things can be declared twice

#given a list of lists of tokens each list = tokens
from error import *
from tokens import *

def declaration_check(listy):
    is_declared=["" for line in listy]
    for i,line in enumerate(listy):
            if isinstance(line[0], Variable) and isinstance(line[1], ISA):
                if line[0].label in is_declared:
                    error()
                else:
                    is_declared[listy.index(line)]=line[0].label




    for i,line in enumerate(listy):
        if line[0].label in is_declared[:(listy.index[i+1])]:
            pass
        else:
            error()
