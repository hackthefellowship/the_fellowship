from error import *
import sys, inspect

def concat_doubles(line):
    for i in range(len(line)):
        if line[i] == 'is':
            s = ""
            try:
                s = line[i+1]
            except:
                error()
            if s == 'a' or s == 'an' or 'with':
                line[i] = line[i] + ' ' + s
                return concat_doubles(line[:i+1] + line[i+2:])
    return line

            

def tokeniseLine(line):
    line = line.strip().split(' ')
    line = concat_doubles(line)


    return line


def lex(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()

    lines = list(map(tokeniseLine, lines))
    return lines

def print_classes():
    for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
        print (name, obj)