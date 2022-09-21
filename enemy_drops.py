import json
import os
import sys
from pprint import pprint
import glob
import time

enemies = glob.glob('.\\enemies\\**\\*.json')
# print(enemies)


for enemy in enemies:
    # print(enemy)
    json_data = json.load(open(enemy, 'r'))
    # pprint(json_data)
    # break
    try:
        # print(enemy)
        # print(json_data['itemDrops'])
        for i in json_data['itemDrops']:
            i['prob'] = 1
            i['rank'] = ''
        for j in json_data['items']:
            j['prob'] = 1
            j['rank'] = ''
        file = open(enemy, 'w')
        file.write(json.dumps(json_data))
    except:
        print('unable to modify', enemy)

