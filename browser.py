import requests
from rich import print

r = requests.get('https://swapi.dev/api/planets/1/')
planet = r.json()
print(planet["name"])