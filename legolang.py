#!/usr/bin/env python
import sys
import lexer
import parser
import names
import create_adventurer

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("FOOL OF A TOOK\npsst, it's <%s> <file.ll>" % sys.argv[0])
        exit()
    tokens = lexer.lex(sys.argv[1])
    world = parser.parse(tokens)
    #names.declaration_check(tokens)
    characters = create_adventurer.create_adventurer(tokens)
    print (characters)
