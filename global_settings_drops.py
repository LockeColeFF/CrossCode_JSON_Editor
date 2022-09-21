import json
import os
import sys
from pprint import pprint
import glob
import time

json_data = json.load(open('./enemies//global-settings.json', "r"))

for entity_name in json_data["ENTITY"]["ItemDestruct"]:
    for info in json_data["ENTITY"]["ItemDestruct"][entity_name]["items"]:
        info['prob'] = .75
json.dump(json_data, open("enemies/global-settings.json", 'w'))
