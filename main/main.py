# All rights reserved to Jack Strating #

import requests
import os
import json as jsn
import time
from datetime import datetime as dt
import sys

# cwd = os.path.dirname(os.path.realpath(__file__)) + '\\config.json'

def main():
    DIRECTORY = __file__.replace('main.py','config.json')
    filename=open(DIRECTORY,'r')
    load_json = jsn.load(filename)

    try:
        if load_json['username'] == "":
            print("ERR: Please insert a valid username in the category of 'username' in 'config.json'" )
            time.sleep(5)
            sys.exit()
        elif load_json['url'] == "":
            print("ERR: Please insert a valid url in the category of 'url' in 'config.json'")
            time.sleep(5)
            sys.exit()
        elif load_json['message'] == "":
            print("ERR: Please insert a valid url in the category of 'message' in 'config.json'")
            time.sleep(5)
            sys.exit()
    except TypeError:
            print("ERR: Problem parsing 'config.json' file.")


    data = {
        'username': load_json['username'],
        'avatar_url': load_json['avatar_url'],
        'content': load_json['message'],
    }
    result = requests.post(load_json['url'], json=data)
    if load_json['loop'] == "True":
        while True:
            time.sleep(1)
            print(result)
    elif load_json['loop'] == "False":
        print(result)


    with open(os.path.dirname(os.path.realpath(__file__)) + '\\logs.txt', 'w') as log:
            log.write(str(dt.now())+': ' + '<Response' + '['+str(result.status_code)+']>')

if __name__ == "__main__":
    main()
