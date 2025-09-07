#basic functionality CRUD
#C - add a new Person with name and contact number
#R - print the list of current People on the list
#U - allow you to modify the contacts
#D - be able to delete a contact
#S - search a particular Person

#considerations:
#   save to .json file
#   alphabetic ordering list
#   search by name or number, message if can't be found

import json
import os
import re

#add a new person
class Person:
    def __init__(self, init_type="default", p_name=None, p_number=None, json_data=None):
        if init_type == "default":
            self.name = p_name
            self.number = p_number
        elif init_type == "json":
            self.name = json_data["name"]
            self.number = json_data["number"]

    def __str__(self):
        return f"\t{self.name}\t\t{self.number}"

    def to_json(self):
        return {
                "name" : self.name,
                "number" : self.number
                }

FILE_NAME = "contact_keeper_cli.json"
file = None
def initialize():
    try:
        file = open(FILE_NAME, "rt")
    except:
        file = open(FILE_NAME, "xt")
        file.close()
    finally:
        file.close()
initialize()

def save(person):
    file = open(FILE_NAME, "at")
    file.write(json.dumps(person.to_json()))
    file.close()

def print_file():
    print("\t~~~ CONTACT KEEPER ~~~\t")
    with open(FILE_NAME) as f:
        for line in f:
            #print(line.readline())
            contact_json = Person(init_type = "json", json_data = json.loads(line))
            print(contact_json)

def add():
    new_name = input("Name = ")
    new_number = input("Number = ")
    new_person = Person(init_type="default",p_name = new_name, p_number = new_number)
    print(json.dumps(new_person.to_json()))
    save(new_person)

def search():
    search_term = input("Search > ")
    search_reg = ".+" + search_term  + ".*"
    with open(FILE_NAME) as f:
        search_result = []
        for line in f:
            res = re.search(search_reg, line)
            if res:
                search_result.append(res)
        clear_screen()
        for res in search_result:
            print(res)
    input("[ENTER to Continue]")

def clear_screen():
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def option_menu():
    option = None
    while option != "E":
        clear_screen()
        print_file()
        print("\n\n\n")
        print("[A]dd\t[S]earch\t[M]odify\t[D]elete\t[E]xit")
        option = input("> ").upper()
        match option:
            case "A":
                add()
            case "S":
                search()

option_menu()
