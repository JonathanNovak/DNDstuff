#A random character generator for fifth edition of dungeons and dragons
#Author: Jonathan Novak
import random
import requests
import json
import argparse
from equipment import *
from spells import *
from skills import *

d4 = random.randint(1,5)
d6 = random.randint(1,7)
d8 = random.randint(1,9)
d10 = random.randint(1,11)
d12 = random.randint(1,13)
d20 = random.randint(1,21)
d100 = random.randint(1,101)

race_num = random.randint(1,9)
class_num = random.randint(1,12)
parser = argparse.ArgumentParser()
parser.add_argument('-c','--name',action ='store')
args = parser.parse_args()
back_num = random.randint(1,18)
print("auto character generator for dnd 5e")
level = 1

#basic set of dice
def d4():
    return random.randint(1,4)
def d6():
    return random.randint(1,6)
def d8():
    return random.randint(1,8)
def d10():
    return random.randint(1,10)
def d12():
    return random.randint(1,12)
def d20():
    return random.randint(1,20)
def d100():
    return random.randint(1,100)

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

def race(race_num):
    switch = {
        1:  "Dwarf",
        2:  "Elf",
        3:  "Halfling",
        4:  "Human",
        5:  "Dragonborn",
        6:  "Gnome",
        7:  "Half-Elf",
        8:  "Half-orc",
        9:  "Tiefling"
    }
    return switch.get(race_num, "null")

def background(back_num):
    switch = {
        1:  "Acolyte",
        2:  "Charlatan",
        3:  "Criminal",
        4:  "Entertainer",
        5:  "Folk Hero",
        6:  "Gladiator",
        7:  "Guild Artisan",
        8:  "Guild Merchant",
        9:  "Hermit",
        10: "Knight",
        11: "Noble",
        12: "Outlander",
        13: "Pirate",
        14: "Sage",
        15: "Sailor",
        16: "Soldier",
        17: "Spy",
        18: "Urchin"
    }
    return switch.get(back_num, "null")

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
        class_f_range2 = 416

    classfeat=random.randint(class_f_range,class_f_range2)

    r_feat = requests.get('http://www.dnd5eapi.co/api/features/%s'%(str(classfeat)))
    d_feat = json.loads(r_feat.content.decode('utf-8'))

    if "level" in d_feat:
        if not d_feat["level"]:
            char_feature(classname, level)
        while(int(d_feat["level"]) > level):
            classfeat=random.randint(class_f_range,class_f_range2)
            r_feat = requests.get('http://www.dnd5eapi.co/api/features/%s'%(str(classfeat)))
            d_feat = json.loads(r_feat.content.decode('utf-8'))
            while not d_feat:
                print(classfeat)
                classfeat=random.randint(class_f_range,class_f_range2)
                r_feat = requests.get('http://www.dnd5eapi.co/api/features/%s'%(str(classfeat)))
                d_feat = json.loads(r_feat.content.decode('utf-8'))
    else:
        char_feature(classname, level)

    print ("\nFEAT: " + str(d_feat["name"]))
    print ("desc: " + str(d_feat["desc"]))

def stats(race):
    statlist = []
    for x in range(6):
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        roll3 = random.randint(1,6)
        roll4 = random.randint(1,6)
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

def otherstats(classname,level):
    if (classname == "Barbarian"):
        basehp = 12
    elif(classname == "Fighter" or classname == "Paladin" or classname == "Ranger"):
        basehp = 10
    elif(classname == "Bard" or classname == "Cleric" or classname == "Druid" or classname == "Monk" or classname == "Rogue" or classname == "Warlock"):
        basehp = 8
    elif(classname == "Sorcerer" or classname == "Wizard"):
        basehp = 6
    if(level > 1):
        levelhp = basehp
        for i in range(level-1):
            levelhp += random.randint(1,basehp)
        return levelhp
    else:
        return basehp

def alignment():
    alignment_num = random.randint(1,3)
    switch = {
        1:  "Lawful",
        2:  "Neutral",
        3:  "Chaotic",
    }
    alignment1 = str(switch.get(alignment_num, "null"))

    alignment_num = random.randint(1,3)
    switch = {
        1:  "Good",
        2:  "Neutral",
        3:  "Evil",
    }
    alignment2 = str(switch.get(alignment_num, "null"))
    alignment = alignment1 + " " + alignment2
    if (alignment == "Neutral Neutral"):
        alignment = "True Neutral"
    return alignment

def bonus(stat):
        switch = {
            1:  "-5",
            2:  "-4",
            3:  "-4",
            4:  "-3",
            5:  "-3",
            6:  "-2",
            7:  "-2",
            8:  "-1",
            9:  "-1",
            10: "+0",
            11: "+0",
            12: "+1",
            13: "+1",
            14: "+2",
            15: "+2",
            16: "+3",
            17: "+3",
            18: "+4",
            19: "+4",
            20: "+5"
        }
        return switch.get(stat, "null")


classname= char_class(class_num)
race = race(race_num)
r_race = requests.get('http://www.dnd5eapi.co/api/races/%s'%(str(race_num)))
d_race = json.loads(r_race.content.decode('utf-8'))

strength = stats(race_num)[0]
dex = stats(race_num)[1]
con = stats(race_num)[2]
intel = stats(race_num)[3]
wis = stats(race_num)[4]
cha = stats(race_num)[5]

print ("Race: " + race)
print ("Size: " + str(d_race["size"]))
print ("Class: " + classname)
print ("Alignment: " + alignment())
print ("Stats: str:" + str(strength) + " dex: " + str(dex) + " con: " + str(con) + " int: " + str(intel) + " wis: " + str(wis) + " cha: " + str(cha) )
print ("HP: "+ str(otherstats(classname,level)))
print ("Gold: " + str(gold(class_num)))
print ("Background: " + background(back_num) + "\n")
print("Skills:")
skills(bonus(strength),bonus(dex),bonus(con),bonus(intel),bonus(wis),bonus(cha),back_num)
char_feature(classname,level)
print ("\nProficiencies: " + str(start_proficiencies(race_num)))
print ("Traits: " + str(traits(race_num)))
if(class_num == 12 and level >= 3):
    spell_school()


r_spells = requests.get('http://dnd5eapi.co/api/spells/1')
data = json.loads(r_spells.content.decode('utf-8'))
