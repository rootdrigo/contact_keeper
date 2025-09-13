#basic functionality CRUD + S
#C - add a new Person with name and contact number
#R - print the list of current People on the list
#U - allow you to modify the contacts
#D - be able to delete a contact
#S - search a particular Person

#considerations:
# [x]  save to .json file
# [x]  alphabetic ordering list
# [x]  search by any field, message if can't be found

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
    print("\t\t\t~~~ CONTACT KEEPER ~~~")
    with open(FILE_NAME) as f:
        for line in f:
            #print(line.readline())
            contact_json = Person(init_type = "json", json_data = json.loads(line))
            print(contact_json)

def sort_file():
    lines, sorted_lines = [], []
    with open(FILE_NAME) as f:
        for line in f:
            lines.append(line)
        sorted_lines = sorted(lines)
    with open(FILE_NAME,"wt") as f:
        for s_line in sorted_lines:
            f.write(s_line)

def add():
    new_name = input("Name = ")
    new_phone = input("Phone = ")
    new_email = input("Email = ")
    new_person = Person(init_type="default",p_name = new_name, p_phone = new_phone, p_email = new_email)
    print(json.dumps(new_person.to_json()))
    save(new_person)
    sort_file()

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
            if mode in ["Modify", "Delete"]:
                return None, None
        elif mode == None:
            p_person = None
            for res in search_result:
                p_person = Person(init_type="json", json_data=json.loads(res.group(0)))
                print(p_person)
            input("[press ENTER to Continue]")
        elif mode in ["Modify", "Delete"]:
            return search_result_selection(search_result)

def search_result_selection(search_result):
    if search_result:
        p_person = None
        p_person_json = None
        for idx, res in enumerate(search_result):
            p_person = Person(init_type="json", json_data=json.loads(res.group(0)))
            print(idx+1,"- ", p_person)
        selection = input("select the Contact Index or C to cancel > ")
        if selection in ["c", "C"]:
            return None, None
        for idx, res in enumerate(search_result):
            if idx == (int(selection) - 1):
                p_person = Person(init_type="json", json_data=json.loads(res.group(0)))
                p_person_json = res.group(0)
        clear_screen()
        print(p_person)
        return p_person_json, p_person
    return None, None

def modify():
    target_json, p_target = search(mode = "Modify")
    if target_json != None:
        new_name = input("\nEnter new Name or ENTER to skip > ")
        new_name = p_target.name if new_name == "" else new_name
        new_phone = input("Enter new Phone or ENTER to skip > ")
        new_phone = p_target.phone if new_phone == "" else new_phone
        new_email = input("Enter new Email or ENTER to skip > ")
        new_email = p_target.email if new_email == "" else new_email
        new_person = Person(init_type="default",p_name = new_name, p_phone = new_phone, p_email = new_email)
        with open(".aux.json","wt") as aux_f:
            with open(FILE_NAME) as f:
                for line in f:
                    if line.rstrip() == target_json.rstrip():
                        print("found the one to modify")
                        aux_f.write(json.dumps(new_person.to_json()))
                        aux_f.write("\n")
                    else:
                        aux_f.write(line)
        os.remove(FILE_NAME)
        os.rename(".aux.json",FILE_NAME)

def delete():
    target_json, p_target = search(mode = "Delete")
    if target_json != None:
        with open(".aux.json","wt") as aux_f:
            with open(FILE_NAME) as f:
                for line in f:
                    if line.rstrip() != target_json.rstrip():
                        aux_f.write(line)
        os.remove(FILE_NAME)
        os.rename(".aux.json",FILE_NAME)

def clear_screen():
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def option_menu():
    clear_screen()
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
