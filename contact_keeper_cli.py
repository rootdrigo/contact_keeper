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
    def __init__(self, init_type="default", p_name=None, p_phone=None, p_email=None, json_data=None):
        if init_type == "default":
            self.name = p_name
            self.phone = p_phone
            self.email = p_email
        elif init_type == "json":
            self.name = json_data["name"]
            self.phone = json_data["phone"]
            self.email = json_data["email"]

    def __str__(self):
        return f"\t{self.name}\t\t{self.phone}\t\t{self.email}"

    def to_json(self):
        return {
                "name" : self.name,
                "phone" : self.phone,
                "email" : self.email
                }

FILE_NAME = "contacts.json"
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
    file.write("\n")
    file.close()

def print_file():
    print("\t\t~~~ CONTACT KEEPER ~~~")
    with open(FILE_NAME) as f:
        for line in f:
            #print(line.readline())
            contact_json = Person(init_type = "json", json_data = json.loads(line))
            print(contact_json)

def add():
    new_name = input("Name = ")
    new_phone = input("Phone = ")
    new_email = input("Email = ")
    new_person = Person(init_type="default",p_name = new_name, p_phone = new_phone, p_email = new_email)
    print(json.dumps(new_person.to_json()))
    save(new_person)

def search(mode=None):
    search_term = input("Search > ")
    search_reg = ".+" + search_term  + ".*"
    search_result = []
    with open(FILE_NAME) as f:
        for line in f:
            res = re.search(search_reg, line)
            if res:
                search_result.append(res)
        clear_screen()
        if len(search_result) == 0:
            print("No entry found")
            input("[press ENTRE to Continue]")
        elif mode == None:
            p_person = None
            for res in search_result:
                p_person = Person(init_type="json", json_data=json.loads(res.group(0)))
                print(p_person)
            input("[press ENTER to Continue]")
        elif mode in ["Modify", "Delete"]:
            return search_result

def modify():
    search_result = search(mode = "Modify")
    if search_result:
        p_person = None
        for idx, res in enumerate(search_result):
            p_person = Person(init_type="json", json_data=json.loads(res.group(0)))
            print(idx+1,"- ", p_person)
        if len(search_result) > 1:
            selection = input("select the Index to modify or C to cancel")
            if selection in ["c", "C"]:
                return None
            for idx, res in enumerate(search_result):
                if idx == (selection - 1):
                    p_person = Person(init_type="json", json_data=json.loads(res.group(0)))
        clear_screen()
        print(p_person)
        new_name = input("Enter new Name or ENTER to skip")
        new_phone = input("Enter new Phone or ENTER to skip")
        new_email = input("Enter new Email or ENTER to skip")
        input("[press ENTER to Continue]")

def delete():
    search_result = search(mode = "Delete")
    if search_result:
        pass

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
            case "M":
                modify()
            case "D":
                delete()

option_menu()
