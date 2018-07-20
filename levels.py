#Class to manage character levels
#Author: Jonathan Novak
import random
import requests
import json
import argparse

def level_display(classname,level):
    classname = classname.lower()
    spellslots = []
    r_level = requests.get('http://www.dnd5eapi.co/api/classes/%s/level/%i'%(classname,level))
    d_level = json.loads(r_level.content.decode('utf-8'))
    prof_bonus = str(d_level["prof_bonus"])
    ability_bonus = str(d_level["ability_score_bonuses"])
    features = str([r['name'] for r in d_level['features']])
    print("Spell Slots: ")
    spellslots = d_level['spellcasting']
    print(spellslots)
    print("Proficiency Bonus: " + prof_bonus)
    print("Ability Bonus: " + ability_bonus)
    print("Features: " + features)
