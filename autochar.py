#A random character generator for fifth edition of dungeons and dragons
#Author: Jonathan Novak
import random
import requests
import json
import argparse

d4 = random.randint(1,5)
d6 = random.randint(1,7)
d8 = random.randint(1,9)
d10 = random.randint(1,11)
d12 = random.randint(1,13)
d20 = random.randint(1,21)
d100 = random.randint(1,101)

parser = argparse.ArgumentParser()
parser.add_argument('-c','--name',action ='store')
args = parser.parse_args()
print("auto character generator for dnd 5e")
class_num = random.randint(1,12)
level = 1

def char_class(class_num):
    switch = {
        1:  "Barbarian",
        2:  "Bard",
        3:  "Cleric",
        4:  "Druid",
        5:  "Fighter",
        6:  "Monk",
        7:  "Paladin",
        8:  "Ranger",
        9:  "Rogue",
        10: "Sorcerer",
        11: "Warlock",
        12: "Wizard",
    }
    return switch.get(class_num, "null")

def char_feature(classname,level):
    if(classname == "Barbarian"):
        class_f_range = 1
        class_f_range2 = 25
    elif(classname == "Bard"):
        class_f_range = 25
        class_f_range2 = 71
    elif(classname == "Cleric"):
        class_f_range = 71
        class_f_range2 = 101
    elif(classname == "Druid"):
        class_f_range = 101
        class_f_range2 = 131
    elif(classname == "Fighter"):
        class_f_range = 131
        class_f_range2 = 160
    elif(classname == "Monk"):
        class_f_range = 160
        class_f_range2 = 191
    elif(classname == "Paladin"):
        class_f_range = 191
        class_f_range2 = 220
    elif(classname == "Ranger"):
        class_f_range = 220
        class_f_range2 = 260
    elif(classname == "Rogue"):
        class_f_range = 260
        class_f_range2 = 303
    elif(classname == "Sorcerer"):
        class_f_range = 303
        class_f_range2 = 340
    elif(classname == "Warlock"):
        class_f_range = 340
        class_f_range2 = 400
    elif(classname == "Wizard"):
        class_f_range = 400
        class_f_range2 = 417

    classfeat=random.randint(class_f_range,class_f_range2)

    r_feat = requests.get('http://www.dnd5eapi.co/api/features/%s'%(str(classfeat)))
    feat = json.loads(r_feat.content.decode('utf-8'))

    while(str(feat["level"]) > str(level)):
        classfeat=random.randint(class_f_range,class_f_range2)
        r_feat = requests.get('http://www.dnd5eapi.co/api/features/%s'%(str(classfeat)))
        feat = json.loads(r_feat.content.decode('utf-8'))

    print ("FEAT: " + str(feat["name"]))
    print ("desc: " + str(feat["desc"]))

def stats():
    statlist = []
    for x in range(6):
        roll1 = random.randint(1,7)
        roll2 = random.randint(1,7)
        roll3 = random.randint(1,7)
        roll4 = random.randint(1,7)
        min = roll1
        if(roll2 < min):
            min = roll2
        if(roll3 < min):
            min = roll3
        if(roll4 < min):
            min = roll4
        stat = roll1 + roll2 + roll3 + roll4 - min
        statlist.append(stat)
    return statlist

classname= char_class(class_num)
print (char_class(class_num))
char_feature(classname,level)
print (stats())
r_spells = requests.get('http://dnd5eapi.co/api/spells/1')
data = json.loads(r_spells.content.decode('utf-8'))
