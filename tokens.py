

filein = open("actions.txt","r")
lines = filein.readlines()
filein.close()

actions = []
interactions = []
races = []
possessions = []

for line in lines:
    line = line.strip()
    name, lst = line.split(":")
    lst = lst.split(",")
    if name == "actions":
        actions = [l for l in lst]
    if name == "interactions":
        interactions = [l for l in lst]
    if name == "races":
        races = [l for l in lst]
    if name == "possessions":
        possessions = [l for l in lst]

print(possessions)
       
    
class Action:

    def __init__(self, label):

        self.valid = self.check_valid(label)
        self.label = label

    def check_valid(self, label):

        if label in actions:

            return True

        else:

            return False
        

class Interaction:

    def __init__(self, label):

        self.valid = self.check_valid(label)
        self.label = label

    def check_valid(self,label):

        if label in interactions:

            return True

        else:

            return False


class Type:
    
    def __init__(self, label):

        self.valid = self.check_valid(label)
        self.label = label

    def check_valid(self, label):

        if label in races:

            return True

        else:

            return False

class Possesion:

    def __init__(self, label):

        self.valid = self.check_valid(label)
        self.label = label


    def check_valid(self,label):

        if label in possessions:

            return True

        else:

            return False

class ISA:

    def __init__(self, label):

        self.valid = self.check_valid(label)
        self.label = label

    def check_valid(self,label):

        if label == "is a":

            return True

        else:

            return False

class ISIN:

    def __init__(self, label):

        self.valid = self.check_valid(label)
        self.label = label

    def check_valid(self,label):

        if label == "is in":

            return True

        else:

            return False    

class Variable:

    def __init__(self,label):

        self.valid = True
        self.label = label