# main file for the interpreter
import sys
import lexer
import parser
import names
import character

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("FOOL OF A TOOK\npsst, it's <%s> <file.ll>" % sys.argv[0])
        exit()
    tokens = lexer.lex(sys.argv[1])
    world = parser.parse(tokens)
    names.declaration_check(tokens)
    characters = character.create_characters(tokens)
