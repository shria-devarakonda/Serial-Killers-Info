# Object for serial killer data display
import sqlite3 as sl


class SerialKiller:
    def __init__(self, idnum, name, victims_count, legacy, moniker, agearrest):
        self.name = name
        self.idnum = idnum
        self.victims_count = victims_count
        self.legacy = legacy
        self.moniker = moniker
        self.agearrest = agearrest

    def id_num(self):
        return "ID: {}.\n".format(self.idnum)

    def nameofsk(self):
        return "His name was {}.\n".format(self.name)
      
    def vicnum(self):
        return "He killed {} people.\n".format(self.victims_count)
          
    def bestknown(self):
        return "He was best known for {}.\n".format(self.legacy)
      
    def nickname(self):
        return "He was also known as {}.\n".format(self.moniker)
      
    def arrestedage(self):
        return "He was arrested when he was {}.".format(self.agearrest)

sk = []
sk_name = []
con = sl.connect('serial_killer.db')
with con:
     data = con.execute("SELECT * FROM KILLERS")
     for row in data:
        sk.append(row)
     data = con.execute("SELECT name FROM KILLERS")
     for row in data:
        sk_name.append(row)
import re
a = re.sub("]*\\[*\\(*\\)*'*", '', str(sk_name))
c = re.sub("(,)", '|', a)
print(c+"|")
name = input("Who would you like to learn about? Enter any of the names between the '||'s above. Partial name is "
             "fine too.\nFor instance, you can type jeff or dahm for Jeffrey Dahmer.\nIf there is not much "
             "above, please add some data with addserialkiller.py file!\n").lower()


for row in sk:
    if str(name) in str(row).lower():
        name = SerialKiller(*list(row))
        print(name.id_num(), name.nameofsk(), name.vicnum(), name.bestknown(), name.nickname(), name.arrestedage())
