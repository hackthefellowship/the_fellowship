import traceback
import sys
DEBUG = True
def error():
    print ("FOOL OF A TOOK!")
    if DEBUG:
        traceback.print_stack(file=sys.stdout)
    exit()