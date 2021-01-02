import requests
from rich import print
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich import box
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

def clear(): 
    # for windows 
    if os.name == 'nt': 
        os.system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        os.system('clear')

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

def main_screen():
    clear()
    print("")
    print("")
    print(".        .               .       .     .            .")
    print("   .           .        .                     .        .            .")
    print("             .               .    .          .              .   .         .")
    print("               _________________      ____         __________")
    print(" .       *    /                 |    /    \    .  |          \\")
    print("     .       /    ______   _____| . /      \      |    ___    |     .     .")
    print("             \    \    |   |       /   /\   \     |   |___>   |")
    print("           .  \    \   |   |      /   /__\   \  . |         _/               .")
    print(" .     ________>    |  |   | .   /            \   |   |\    \_______    .")
    print("      |            /   |   |    /    ______    \  |   | \           |")
    print("      |___________/    |___|   /____/      \____\ |___|  \__________|    .")
    print("  .     ____    __  . _____   ____      .  __________   .  _________")
    print("       \    \  /  \  /    /  /    \       |          \    /         |      .")
    print("        \    \/    \/    /  /      \      |    ___    |  /    ______|  .")
    print("         \              /  /   /\   \ .   |   |___>   |  \    \\")
    print("   .      \            /  /   /__\   \    |         _/.   \    \            +")
    print("           \    /\    /  /            \   |   |\    \______>    |   .")
    print("            \  /  \  /  /    ______    \  |   | \              /          .")
    print(" .       .   \/    \/  /____/      \____\ |___|  \____________/  LS")
    print("                               .                                        .")
    print("     +                           .         .               .                 .")
    print("                .                                   .            .")
    print("")
    options = [
        Panel("P: People"),
        Panel("F: Films")
    ]
    print(Columns(options))
    choice = input("Make your choice ('q' to quit): ").lower()
    if choice == "p":
        people_screen()
    if choice == "f":
        films_screen()

def people_screen():
    clear()
    people = make_request("people/")
    render_people(people)

def films_screen():
    clear()
    films = make_request("/films/")
    render_films(films)

def render_films(films):
    table = Table(show_header=True, box=box.SIMPLE_HEAVY)
    table.add_column("Episode ID", width=12)
    table.add_column("Title")
    table.add_column("Release date")
    for film in films["results"]:
        table.add_row(
            str(film["episode_id"]),
            film["title"],
            film["release_date"]
        )
    console = Console()
    console.print(table)

def render_people(people):
    table = Table(show_header=True, box=box.SIMPLE_HEAVY)
    table.add_column("Name", width=12)
    table.add_column("homeworld")
    table.add_column("number of films they are in")
    for person in people["results"]:
        table.add_row(
            person["name"],
            person["homeworld"],
            str(len(person["films"]))
        )
    console = Console()
    console.print(table)

setup()
main_screen()