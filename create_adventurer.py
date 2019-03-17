from hackthefellowship import *
from tokens import *
from error import *

lower = list(map(chr, range(97, 123)))
upper = list(map(chr, range(65, 91)))

def make_tolkein_happy(word): # ie check grammar correct for first letter capital and rest lower case

    if len(word) < 2:
        error()

    if word[0] not in upper:
        error()

    word = word[1:]

    for w in word:
        if w not in lower:
            error()


def create_adventurer(lst):

    adventurers = []
    other = []

    for l in lst:
        if len(l) > 1:

            if isinstance(l[1], ISA):

                make_tolkein_happy(l[0].label)

                if l[2].label == "hobbit":
                    adventurers.append(hobbit(l[0].label)) 
                if l[2].label == "orc":
                    adventurers.append(orc(l[0].label))
                if l[2].label == "elf":
                    adventurers.append(elf(l[0].label))
                if l[2].label == "dwarf":
                    adventurers.append(dwarf(l[0].label))
                if l[2].label == "human":
                    adventurers.append(human(l[0].label))
                if l[2].label == "wizard":
                    adventurers.append(wizard(l[0].label))

            else:

                other.append(l)
        else:
            other.append(l)

    return adventurers, other