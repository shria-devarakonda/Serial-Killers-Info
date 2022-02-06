

class SerialKiller:
    def __init__(self, name, victims_count, mental_disability, legacy, moniker, agearrest):
        self.name = name
        self.victims_count = victims_count
        self.mental_disability = mental_disability
        self.legacy = legacy
        self.moniker = moniker
        self.agearrest = agearrest

    def nameofsk(self):
        return " His name was {}.\n".format(self.name)
      
    def vicnum(self):
        return "He killed {} people.\n".format(self.victims_count)
      
    def mental(self):
        if self.mental_disability:
            return "He had a mental disability.\n"
        else:
            return "He had no mental disability.\n"
          
    def bestknown(self):
        return "He was best known for {}.\n".format(self.legacy)
      
    def nickname(self):
        return "He was also known as {}.\n".format(self.moniker)
      
    def arrestedage(self):
        return "He was arrested when he was {}.".format(self.agearrest)


jeff =["Jeffrey Dahmer", 17, False, "trying to rip out a victims heart from his chest", "The Milwaukee Monster", 32]
ed =["Ed Kemper", 10, True, "decapitating his mother's head and engaging in irrumatio with it", "The Co-ed Killer", 25]
ted = ["Ted Bundy", 30, False, "being deceitfully charming and evading arrest many times", 'The Lady Killer', 29]
john = ["John Wayne Gacy", 33, False, "dressing like a clown and killing his victims", 'Pogo the Clown', 36]
richard = ["Richard Ramirez", 13, True, "being a satan worshipper and having a large female fan following after arrest", 'The Night Stalker', 25]
dahmer = SerialKiller(*jeff)
kemper = SerialKiller(*ed)
bundy = SerialKiller(*ted)
gacy = SerialKiller(*john)
ramirez = SerialKiller(*richard)

def infosk(name):
    print(name.nameofsk(), name.vicnum(), name.mental(), name.bestknown(), name.nickname(), name.arrestedage())

sk = ["dahmer", "kemper", "bundy", "gacy", "ramirez"]
print([i for i in sk])
query = input("Who would you like to learn about? (Enter any of the last names above) \n").lower()

try:
    infosk(eval(query))
except:
    print("Sorry, no information on {}.".format(query))
