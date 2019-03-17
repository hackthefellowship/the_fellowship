list_of_stats = []

class character(object):
    def __init__(self,race,name,health,damage):
        self.race = race
        self.name = name
        self.health = health
        self.possesions = []
        self.journey = []
        self.damage = damage
        self.friends = []
        self.weapon = ""

    def fights(self,opponent, weapon):
        if weapon in self.possesions:
            if self.damage*weapon.stats < opponent.damage:
                self.health -= (opponent.damage-self.damage*weapon.stats)

    def eats(self,food):
        if food in self.possesions:
            if "lembras bread" in self.possesions:
                self.health= self.health*food.stats
            else:
                self.health+= food.stats
                
    def heals(friend):
        if friend in self.friends:
            friend.health +=20

    def finds(self,thing):
        stts = list_of_stats[list_of_items.index(thing)]
        self.possesions.append(thing)
    def loses(self,thing):
        if thing in self.possesions:
            self.possesions.remove(thing)

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

    def joins(self,friends):
        for f in friends:
            self.friends.append(f)
            f.friends.append(self.name)

    def leaves(self,friends):
        for f in friends:
            self.friends.remove(f)
            f.friends.remove(self.name)

    def if_statement(self,condition, action):
        if condition:
            action

    def while_statement(self,condition, action):
        while condition:
            action

    def wears_ring(self):
        print(self.health)

    def writes_story(self):
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
        super(elf, self).__init__("elf",name,10000,20)

class dwarf(character):
    def __init__(self,name):
        super(dwarf, self).__init__("dwarf",name,20,50)

class human(character):
    def __init__(self,name):
        super(human, self).__init__("human",name,50,50)

class orc(character):
    def __init__(self,name):
        super(orc, self).__init__("orc",name,100,100)