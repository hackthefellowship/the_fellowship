from error import *
from tokens import *

classes = [Move, Action, Interaction, Type, Possesion, Location, ISA, Sleep, Death, End, Plan, Variable]


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
            if lookfor(line, i, 'a') or lookfor(line, i, 'an') or lookfor(line, i, 'in') or lookfor(line, i, 'amazed') or lookfor(line, i, 'going'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'lembas':
            if lookfor(line, i, 'bread'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'second':
            if lookfor(line, i, 'breakfast'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'afternoon':
            if lookfor(line, i, 'tea'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'travels':
            if lookfor(line, i, 'to'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'journeys':
            if lookfor(line, i, 'to'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'wars':
            if lookfor(line, i, 'with'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'brawls':
            if lookfor(line, i, 'with'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'walks':
            if lookfor(line, i, 'to'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'sleeps':
            if lookfor(line, i, 'deeply'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'finds':
            if lookfor(line, i, 'a'):
                return concat_doubles(qc(line, i))
        if line[i] == 'loses':
            if lookfor(line, i, 'a') or lookfor(line, i ,'the'):
                return concat_doubles(qc(line, i))
        if line[i] == 'Misty':
            if lookfor(line, i, 'Mountains'):
                return concat_doubles(qc(line,i))
        if line[i] == 'Mount':
            if lookfor(line, i, 'Doom'):
                return concat_doubles(qc(line, i))
        if line[i] == 'Helms':
            if lookfor(line, i, 'Deep'):
                return concat_doubles(qc(line, i))
        if line[i] == 'the':
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
        if line[i] == 'writes':
            if lookfor(line, i, 'a'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'writes a':
            if lookfor(line, i, 'story'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'is going':
            if lookfor(line, i, 'on'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'is going on':
            if lookfor(line, i, 'an'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'is going on an':
            if lookfor(line, i, 'adventure'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'is going on an adventure':
            if lookfor(line, i, 'to'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'The':
            if lookfor(line, i, 'Fellowship'):
                return concat_doubles(qc(line, i))
        if line[i] == 'The Fellowship':
            if lookfor(line, i, 'plan'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'The Fellowship plan':
            if lookfor(line, i, 'to'):
                return concat_doubles(qc(line, i))
        if line[i] == 'Until':
            if lookfor(line, i, 'the'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'Until the':
            if lookfor(line, i, 'death'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'Until the death':
            if lookfor(line, i, 'of'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'wears':
            if lookfor(line, i, 'the'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] =='wears the':
            if lookfor(line, i, 'one'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] =='wears the one':
            if lookfor(line, i, 'ring'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'The':
            if lookfor(line, i, 'last'):
                return concat_doubles(qc(line, i))
            else:
                error()    
        if line[i] == 'The last':
            if lookfor(line, i, 'pages'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'The last pages':
            if lookfor(line, i, 'are'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'The last pages are':
            if lookfor(line, i, 'for'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'The last pages are for':
            if lookfor(line, i, 'you'):
                return concat_doubles(qc(line, i))
            else:
                error()
        if line[i] == 'The last pages are for you':
            if lookfor(line, i, 'Sam'):
                return concat_doubles(qc(line, i))
            else:
                error()



    return line



def tokeniseLine(line):
    line = line.strip().split(' ')
    if any(map(lambda z : not (z.isalnum() or '-' in z), line)):
        error()
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

    lines = list(filter(lambda z: len(z.strip()) > 0, lines))
    lines = list(map(tokeniseLine, lines))
    return lines
