

def execute(characters, tokens):
    for line in tokens:
        char = line[0].label
        for c in characters:
            if c.name == char:
                char = c
        print (char)