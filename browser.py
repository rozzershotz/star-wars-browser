import requests
from rich import print
import os.path
import json

def make_request(path):
    cachefile = make_cache_file_name(path)
    if check_file_exists(cachefile):
        return get_cache_data(cachefile)
    response = requests.get("https://swapi.dev/api/" + path)
    json = response.json()
    file1 = open(cachefile,"w+")
    file1.write(response.text)
    file1.close()
    return json

def get_cache_data(file):
    with open(file) as json_file:
        return json.load(json_file)

def setup():
    if os.path.isdir('cache'):
        return
    os.mkdir("cache")

def check_file_exists(file):
    return os.path.isfile(file)

def make_cache_file_name(path):
    strippedpath = path.strip("/").replace("/", ".")
    return "cache/" + strippedpath + ".json"

setup()

planet = make_request('planets/9/')
print(planet["name"])

ship = make_request("starships/9/")
print(ship["name"])