from error import *

items_list = []

filein = open("actions.txt","r")
lines = filein.readlines()
filein.close()

for line in lines:
    line = line.strip()
    name, lst = line.split(":")
    lst = lst.split(",")
    if name == "possessions":
        items_list = [l for l in lst]
    if name == "stats":
        stats_list = [int(l) for l in lst]

class character(object):
    def __init__(self,race,name,health,damage):
        self.race = race
        self.name = name
        self.health = health
        self.possesions = []
        self.journey = []
        self.damage = damage
        self.friends = []
        # self.weapon = ""

    def fights(self,opponent): # opponent will be class
        if self.health > 0 and opponent.health >0:
            if self.health-opponent.damage <0:
                self.health =0
            else:
                self.health -= opponent.damage
            opponent.health -= self.damage


    def eats(self,food): # food will be string
        if food in self.possesions and self.health > 0:
            self.health += stats_list[items_list.index(food)]
        else:
            error()

    def revives(self,friend): # friend will be class
        if friend in self.friends:
            if self.health > 0 and friend.health <= 0 and self.race == 'wizard':
                friend.health = 1


    def finds(self,thing): # thing will be string
        if self.health > 0 and thing in items_list:
            stat_index = items_list.index(thing)
            if stat_index < 5:
                self.damage += stats_list[stat_index]
                self.possesions.append(thing)
            else:
                self.possesions.append(thing)
        else:
            error()

    def loses(self,thing): # thing will be string
        if thing in self.possesions and self.health > 0:
            self.possesions.remove(thing)
            stat_index = items_list.index(thing)
            if stat_index < 5:
                self.damage -= stats_list[stat_index]
        else:
            error()

    def travels(self,location):
        if len(self.friends) == 0:
            self.journey.append(location)
        else:
            self.journey.append(location)
            for f in self.friends:
                f.journey.append(location)

    def naps(self):
        self.journey.append(",")

    def sleeps_deeply(self):
        self.journey.append(".")

    def is_amazed(self):
        self.journey.append("!")

    def ponders(self):
        self.journey.append(" ")

    def joins(self,friend): # friend will be class

        if self.health < 1 :
            error()

        self.friends.append(friend)
        friend.friends.append(self)


    def leaves(self,friend): # friend will be class
        if self.health < 1:
            error()
        self.friends.remove(friend)
        friend.friends.remove(self)

    def if_statement(self,condition, action):
        if condition:
            action

    def while_statement(self,condition, action):
        while condition:
            action

    def wears_ring(self):
        print(self.health)

    def writes_story(self):
        if self.health < 1:
            error()
        list_of_places=["Iron Hills", "Mirkwood","Misty Mountains","Gondor","Mordor","Mount Doom","Eriador","Erebor","Fangorn","Helms Deep","Isengard","Kazad-dum","Rivendell","the Shire","Arnor","Weathertop","Emyn Muil","Minas Tirith","Rohan","Morannon","Grey Havens","Morthond Vale","Ringlo Vale","Bruinen","Andvin", "Erid Luin"]
        alphabet= list(map(chr, range(97,123)))
        lst =[]
        for loc in self.journey:
            if loc in list_of_places:
                lst.append(alphabet[list_of_places.index(loc)])
            else:
                lst.append(loc)
        sentence = ''.join(lst)
        print(sentence)

class hobbit(character):
    def __init__(self,name):
        super(hobbit, self).__init__("hobbit",name,10,1)

class elf(character):
    def __init__(self,name):
        super(elf, self).__init__("elf",name,100,8)

class dwarf(character):
    def __init__(self,name):
        super(dwarf, self).__init__("dwarf",name,80,6)

class human(character):
    def __init__(self,name):
        super(human, self).__init__("human",name,50,4)

class orc(character):
    def __init__(self,name):
        super(orc, self).__init__("orc",name,20,3)

class wizard(character):
    def __init__(self,name):
        super(wizard, self).__init__("wizard",name,150,15)
