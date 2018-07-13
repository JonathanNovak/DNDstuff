#Class to manage equipment, gold, and Proficiencies
#Author: Jonathan Novak
import random
import requests
import json
import argparse

def start_proficiencies(race_num):
    r_prof = requests.get('http://www.dnd5eapi.co/api/races/%s'%(str(race_num)))
    d_prof = json.loads(r_prof.content.decode('utf-8'))
    return [r['name'] for r in d_prof['starting_proficiencies']]

def traits(race_num):
    r_prof = requests.get('http://www.dnd5eapi.co/api/races/%s'%(str(race_num)))
    d_prof = json.loads(r_prof.content.decode('utf-8'))
    return [r['name'] for r in d_prof['traits']]

def gold(class_num):
    money = 0
    if(class_num == 1):
        for i in range(2):
            money += random.randint(1,4)
        money = money * 10
    elif(class_num == 2):
        for i in range(5):
            money += random.randint(1,4)
        money = money * 10
    elif(class_num == 3):
        for i in range(5):
            money += random.randint(1,4)
        money = money * 10
    elif(class_num == 4):
        for i in range(2):
            money += random.randint(1,4)
        money = money * 10
    elif(class_num == 5):
        for i in range(5):
            money += random.randint(1,4)
        money = money * 10
    elif(class_num == 6):
        for i in range(5):
            money += random.randint(1,4)
    elif(class_num == 7):
        for i in range(5):
            money += random.randint(1,4)
        money = money * 10
    elif(class_num == 8):
        for i in range(5):
            money += random.randint(1,4)
        money = money * 10
    elif(class_num == 9):
        for i in range(4):
            money += random.randint(1,4)
        money = money * 10
    elif(class_num == 10):
        for i in range(3):
            money += random.randint(1,4)
        money = money * 10
    elif(class_num == 11):
        for i in range(4):
            money += random.randint(1,4)
        money = money * 10
    elif(class_num == 12):
        for i in range(4):
            money += random.randint(1,4)
        money = money * 10
    return money
