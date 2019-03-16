#make sure thinhs are declared before used
#line after delcares locations
#no things can be declared twice

#given a list of lists of tokens each list = tokens
from error import *

def declaration_check(list):
    is_declared=["" for line in list]
    for i,line in enumerate(list):
            if isinstance(line[0], Variable) and isinstance(line[1], ISA):
                if line[0] in is_declared:
                    error()
                else:
                    is_declared[list.index[line]]=line[0]




    for line in list:
        if line[0] in is_declared[:(list.index[line]+1)]:
            pass
        else:
            error()
