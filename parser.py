import hackthefellowship
from error  import *
from tokens import *

def action_stmt(stmt):
    if not len(stmt) == 1:
        return False
    if not isinstance(stmt[0], Possesion):
        return False

def interaction_stmt(stmt):
    if not len(stmt) == 1:
        return False
    if not isinstance(stmt[0], Variable):
        return False
    return True

def move_stmt(stmt):
    if not len(stmt) == 1:
        return False
    if not isinstance(stmt[0], Location):
        return False
    return True

def sleep_stmt(stmt):
    if not len(stmt) == 0:
        return False
    return True

def isa_stmt(stmt):
    if not len(stmt) == 1:
        return False
    if not isinstance(stmt[0], Type):
        return False
    return True

def var_start(stmt):
    if len(stmt) == 0:
        return False
    if isinstance(stmt[0], Action):
        return action_stmt(stmt[1:])
    if isinstance(stmt[0], Interaction):
        return interaction_stmt(stmt[1:])
    if isinstance(stmt[0], Move):
        return move_stmt(stmt[1:])
    if isinstance(stmt[0], ISA):
        return isa_stmt(stmt[1:])
    if isinstance(stmt[0], Sleep):
        return sleep_stmt(stmt[1:])

def check_statement(stmt):
    if len(stmt) == 0:
        return False
    
    if isinstance(stmt[0], Variable):
        return var_start(stmt[1:])

    # add if/else shizazz
    
    

def parse(tokens):
    for statement in tokens:
        if not check_statement(statement):
            error()

    