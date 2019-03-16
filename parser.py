import hackthefellowship
from error  import *
from tokens import *

def multi_instance(obj, instances):
    if any(map(lambda z : isinstance(obj, z), instances)):
        return True
    else:
        return False

def check_statement(statement):
    if not isinstance(statement[0], Variable):
        error()
    if not multi_instance(statement[1], [Action,ISA,Interaction]):
        error()
    if not multi_instance(statement[2], [Variable,possessions,Location]):
        error()

    if isinstance(statement[1], Action):
        pass
    if isinstance(statement[1], ISA):
        if not isinstance(statement[2], Type):
            error()
    if isinstance(statement[1], Interaction):
        if not isinstance(statement[2], Variable):
            error()
    
    

def parse(tokens):
    for statement in tokens:
        if not check_statement(statement):
            error()

    