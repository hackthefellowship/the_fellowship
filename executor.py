from tokens import *

def execute(characters, tokens):
    i=0
    while i < len(tokens):
        line = tokens[i]
        char = line[0].label
        for c in characters:
            if c.name == char:
                char = c
        print (char)

        if len(line) == 2:
            if line[1].label == "naps":
                char.naps()
            elif line[1].label == "sleeps deeply":
                char.sleeps_deeply()
            elif line[1].label == "is amazed":
                char.is_amazed()
            elif line[1].label == "ponders":
                char.ponders()
        
        if len(line) == 3:
            if isinstance(line[1], Move):
                char.travels(line[2].label)
        i += 1