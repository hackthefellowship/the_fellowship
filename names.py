#make sure thinhs are declared before used
#line after delcares locations
#no things can be declared twice

#given a list of lists of tokens each list = tokens
from error import *
from tokens import *

def declaration_check(listy):
    is_declared=["" for line in listy]
    for line in listy:
            if isinstance(line[0], Variable) and isinstance(line[1], ISA):
                if line[0].label in is_declared:
                    error()
                else:
                    is_declared[listy.index(line)]=line[0].label

    for i,line in enumerate(listy):
        b=i+1
        for t in line:
            if isinstance(t, Variable):
                if t.label in is_declared[:b]:
                    pass
                else:
                    error()
