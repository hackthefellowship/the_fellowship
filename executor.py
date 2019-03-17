from tokens import *
import hackthefelloship

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

            if isinstance(line[1], Action):
                if (line[1].label == "finds") or (line[1].label == "finds the") or (line[1].label == "finds a"):
                    char.finds(line[2].label)
                if (line[1].label == "loses") or (line[1].label == "loses the") or (line[1].label == "loses a"):
                    char.loses(line[2].label)

            if isinstance(line[1], Interaction):
                if (line[1].label == "heals") or (line[1].label == "rehabilitates") or (line[1].label == "treats"):
                    char.heals(line[2].label)
                #have to check that line[2].label is a character for fights, join
                if (line[1].label == "fights") or (line[1].label == "battles") or (line[1].label == "brawls with") or (line[1].label == "stabs") or (line[1].label == "mauls") or (line[1].label == "batters") or (line[1].label == "duels") or (line[1].label == "wars with"):
                    char.fights(line[2].label)
                if (line[1].label == "joins"):
                    char.joins(label[2])
                if (line[1].label == "leaves"):
                    char.leaves(label[2])
                if (line[1].label == "wears the ring"):
                    char.wears_ring()
                if (line[1].label == "writes a story"):
                    char.writes_story()
                #not sure what to do about if_statements+while_statements               
        i+=1
