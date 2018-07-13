import random
import requests
import json
import argparse

def start_proficiencies(race_num):
    r_prof = requests.get('http://www.dnd5eapi.co/api/races/%s'%(str(race_num)))
    d_prof = json.loads(r_prof.content.decode('utf-8'))
    print([r['name'] for r in d_prof['starting_proficiencies']])
