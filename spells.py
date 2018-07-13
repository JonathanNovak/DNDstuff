import random
import requests
import json
import argparse

def spell_school():
    school_sel = random.randint(1,8)
    r_school = requests.get('http://www.dnd5eapi.co/api/magic-schools/%s'%(str(school_sel)))
    d_school = json.loads(r_school.content.decode('utf-8'))
    print("\n"+str(d_school["name"]))
    print(str(d_school["desc"]))
    return str(d_school["name"])
