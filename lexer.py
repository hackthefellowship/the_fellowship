from error import *
from tokens import *

classes = [Action, Interaction, Type, Possesion, Location, ISIN, ISA, Variable]


def lookfor(line, i, s):
    nxt = ""
    try:
        nxt = line[i+1]
    except:
        return False
    if nxt == s:
        return True
    else:
        return False


def concat_doubles(line):
    qc = lambda x, y: x[:y] + [x[y] + ' ' + x[y+1]] + x[y+2:]

    for i in range(len(line)):
        if line[i] == 'is':
            if lookfor(line, i, 'a') or lookfor(line, i, 'an') or lookfor(line, i, 'in'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'Misty':
            if lookfor(line, i, 'Mountains'):
                return concat_doubles(qc(line,i))
        if line[i] == 'Mount':
            if lookfor(line, i, 'Doom'):
                return concat_doubles(qc(line, i))
        if line[i] == 'Helms':
            if lookfor(line, i, 'Deep'):
                return concat_doubles(qc(line, i))
        if line[i] == 'The':
            if lookfor(line, i, 'Shire'):
                return concat_doubles(qc(line, i))
        if line[i] == 'Emyn':
            if lookfor(line, i, 'Muil'):
                return concat_doubles(qc(line, i))
        if line[i] == 'Minas':
            if lookfor(line, i, 'Tirith'):
                return concat_doubles(qc(line, i))
        if line[i] == 'Grey':
            if lookfor(line, i, 'Havens'):
                return concat_doubles(qc(line, i))
        if line[i] == 'Morthond':
            if lookfor(line, i, 'Vale'):
                return concat_doubles(qc(line, i))
        if line[i] == 'Ringlo':
            if lookfor(line, i, 'Vale'):
                return concat_doubles(qc(line, i))
        if line[i] == 'Ered':
            if lookfor(line, i, 'Luin'):
                return concat_doubles(qc(line, i))
        if line[i] == 'Iron':
            if lookfor(line, i, 'Hills'):
                return concat_doubles(qc(line, i))

        

    
    return line

            

def tokeniseLine(line):
    line = line.strip().split(' ')
    line = concat_doubles(line)
    line = list(map(lambda l : [C(l) for C in classes], line))

    result = []
    for l in line:
        for a in l:
            if a.valid:
                result.append(a)
                break
    
    return result


def lex(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()

    lines = list(map(tokeniseLine, lines))
    return lines