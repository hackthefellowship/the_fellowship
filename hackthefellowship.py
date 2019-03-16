list_of_places=[Iron Hills,Mirkwood,Misty Mountains,Gondor,Mordor,Mount Doom,Eriador,Erabor,Fangorn,Helms Deep,Isengard,Kazad-dum,Rivendell,The Shire,Arnor,Weathertop,Emyn Muil,Minas Tirth,Rohan,Morannon,Grey Havens,Morthond Vale,Ringlo Vale,Bruinen,Andvin,Erid Luin]
alphabet= [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
Decode:[zip(list_of_places,alphabet)]

class object:
    def __init__(self,name stats):
        self.name = name
        self.stats = stats

class hobbit(character):
    def __init__(self,name):
        self.name = name;
        self.health = 10;
        self.possesions = []
        self.journey = []
        self.damage = "1"
        self.friends = []
    def fights(opponent, weapon):
        if weapon in self.possesions:
            if self.damage < opponent.damage:
                self.health -= (opponent.damage-self.damage*weapon.stats)
            else:
                self.health += self.health*weapon.stats
        else:
            if self.damage < opponent.damage:
                self.health -= (opponent.damage-self.damage)
            else:
                self.health += self.health
    def eats(food):
        if food in self.possesions:
            if "elven bread" in self.possesions:
                self.health= self.health*food.stats
            else:
                self.health+= food.stats
    def finds(thing):
        if thing in list_of_objects:
            stts = list_of_stats[list_of_objects.index(thing)]
            t = object(self,thing,stts)
            self.possesions.append(t)
    def loses(thing):
        if thing in self.possesions:
            self.possesions.remove(thing)
    def travels(location):
        if location in list_of_places:
            self.journey.append(location)
    def naps():
        self.position.appends(",")
    def sleeps_deeply():
        self.position.appends(".")
    def is_amazed():
        self.position.append("!")


class elves:
    def __init__(self,name):
        self.name = name;
        self.health = 10000;
        self.possesions = []
        self.journey = []
        self.damage = "20"
        self.friends = []
    def fights(opponent, weapon):
        if weapon in self.possesions:
            if self.damage < opponent.damage:
                self.health -= (opponent.damage-self.damage*weapon.stats)
            else:
                self.health += self.health*weapon.stats
        else:
            if self.damage < opponent.damage:
                self.health -= (opponent.damage-self.damage)
            else:
                self.health += self.health
    def eats(food):
        if food in self.possesions:
            if "lembas bread" in self.possesions:
                self.health= self.health*food.stats
            else:
                self.health+= food.stats
    def heals(friend):
        if friend in self.friends:
            friend.health += 20
    def finds(thing):
        if thing in list_of_objects:
            stts = list_of_stats[list_of_objects.index(thing)]
            t = object(self,thing,stts)
            self.possesions.append(t)
    def loses(thing):
        if thing in self.possesions:
            self.possesions.remove(thing)
    def travels(location):
        if location in list_of_places:
            self.journey.append(location)
    def naps():
        self.position.appends(",")
    def sleeps_deeply():
        self.position.appends(".")
    def is_amazed():
        self.position.append("!")

    def if_statement (condition, action):
        if condition:
               action
    def while_statement(condition, action)
            while condition:
                action
