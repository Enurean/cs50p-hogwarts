import requests
import json

from rich.console import Console
console = Console()


def main():
    op = input("Do you wish to enquire about: (1.Wizards, 2.Spells or 3.Potions)? ").lower()
    
    # Wizards
    if op == "1" or op == "wizards":
        first_name = input("What's the first name of the wizard you are interested in?: ")
        last_name = input("And the last name?: ")
        op_wizards = input("What is it that you wish to know about: (1.House, 2.Patronus, 3.Boggart)? " ).lower()

        if op_wizards == "1" or op_wizards == "wizards":
            console.print(get_house(first_name, last_name))
        elif op_wizards == "2" or op_wizards == "patronus":
            console.print(get_patronus(first_name, last_name))
        elif op_wizards == "3" or op_wizards == "boggart":
            console.print(get_boggart(first_name, last_name))

    # Incantations
    if op == "2" or op == "spells":
        op_spells = input("Which spell in particular?: (Press 'L' to check list): " ).lower()
        console.print(get_spells(op_spells))

    # Potions
    if op == "3" or op == "potions":
        op_potions = input("Which potion in particular?: (Press 'L' to check list): " )
        console.print(get_potions(op_potions))


def validate_name(wizard):
    # Validate name format and check in database
    check_char = wizard.replace("-", "")
    check_char = check_char.replace(" ", "")
    
    for char in check_char:
        if not char.isalpha():
            raise ValueError("Invalid name, numbers are not accepted")
        else:
            continue

    # Return validated name
    wizard_joined_name = ''.join(char if char.isalpha() else '-' for char in wizard)
    wizard_name = wizard_joined_name.lower()
    return wizard_name

def validate_spell(spell):
    # Validate spell format and check in database
    check_spell = spell.replace("-", "")
    check_spell = check_spell.replace(" ", "")
    
    for i in check_spell:
        if not i.isalpha():
            raise ValueError("Invalid name, numbers are not accepted")
        else:
            continue

    # Return validated name
    spell_joined_name = ''.join(i if i.isalpha() else '-' for i in spell)
    spell_name = spell_joined_name.lower()
    return spell_name


def validate_potion(potion):
    # Validate spell format and check in database
    check_potion = potion.replace("-", "")
    check_potion = check_potion.replace(" ", "")
    
    for i in check_potion:
        if not i.isalpha():
            raise ValueError("Invalid name, numbers are not accepted")
        else:
            continue

    # Return validated name
    potion_joined_name = ''.join(i if i.isalpha() else '-' for i in potion)
    potion_name = potion_joined_name.lower()
    return potion_name

def get_house(first_name, last_name):
    # Validate name
    wizard = first_name.strip() + " " + last_name.strip()
    wizard_name = validate_name(wizard)

    # Request info about wizard to database
    wizard_db = requests.get(url=f"https://api.potterdb.com/v1/characters/{wizard_name}").json()

    # Check if wizard name is in database and return results
    if wizard_name in json.dumps(wizard_db):
        try:
            house = json.dumps(wizard_db["data"]["attributes"]["house"], sort_keys=True, indent=4)
            if house == "null":
                return f"{wizard.title()} is no wizard"
            return house
        except KeyError:
            return f"{wizard.title()} not found in database"
    else:
        return f"{wizard.title()} not found in database"
    

def get_patronus(first_name, last_name):
    # Validate name
    wizard = first_name.strip() + " " + last_name.strip()
    wizard_name = validate_name(wizard)

    # Request info about wizard to database
    wizard_db = requests.get(url=f"https://api.potterdb.com/v1/characters/{wizard_name}").json()

    # Check if wizard name is in database and return results
    if wizard_name in json.dumps(wizard_db):
        try:
            patronus = json.dumps(wizard_db["data"]["attributes"]["patronus"], sort_keys=True, indent=4)
            if patronus == "null":
                return f"{wizard.title()} has not yet discovered its patronus form"
            else:
                return patronus
        except KeyError:
            return f"{wizard.title()} not found in database"
    else:
        return f"{wizard.title()} not found in database"
    

def get_boggart(first_name, last_name):
    try:
        # Validate name
        wizard = first_name.strip() + " " + last_name.strip()
        wizard_name = validate_name(wizard)

        # Request info about wizard to database
        wizard_db = requests.get(url=f"https://api.potterdb.com/v1/characters/{wizard_name}").json()

        # Check if wizard name is in database and return results
        if wizard_name in json.dumps(wizard_db):
            boggart = json.dumps(wizard_db["data"]["attributes"]["boggart"], sort_keys=True, indent=4)
            if boggart == "null":
                return f"{wizard.title()} has not yet discovered what form a boggart would take"
            else:
                return boggart
        else:
            return f"{wizard.title()} not found in database"
        
    except KeyError:
        return f"{wizard.title()} not found in database"
    

def get_spells(spell):
    # Request list of spells to database
    if spell == "l":
        spells_db = requests.get(url=f"https://api.potterdb.com/v1/spells/").json()
        spells_list = []

        for spell in spells_db["data"]:
            # if str(spell["attributes"]["incantation"]) == "None":
            if str(spell["attributes"]["name"]) == "None":
                continue
            else:
                spells_list.append(spell["attributes"]["name"])

        return spells_list
    
    else:
        # Validate spell
        spell = spell.strip()
        spell_name = validate_spell(spell)

        # Return spell's effect
        spells_db = requests.get(url=f"https://api.potterdb.com/v1/spells/").json()

        for i in spells_db["data"]:
            if i["attributes"]["slug"] == spell_name:
                spell_effect = i["attributes"]["effect"]
            else:
                continue

        # return f"The {spell_name} you submitted is actually an incantation, the spell is called {spell_name}, which causes {spell_effect}"
        return spell_effect
    

def get_potions(potion):
    # Request list of potions to database
    if potion == "l":
        potions_db = requests.get(url=f"https://api.potterdb.com/v1/potions/").json()
        potions_list = []

        for potion in potions_db["data"]:
            if str(potion["attributes"]["name"]) == "None":
                continue
            else:
                potions_list.append(potion["attributes"]["name"])

        return potions_list
    
    else:
        # Validate potion
        potion = potion.strip()
        potion_name = validate_potion(potion)

        # Get potions database
        potions_db = requests.get(url=f"https://api.potterdb.com/v1/potions/").json()

        # Extract and return potion effects
        for i in potions_db["data"]:
            try:
                if i["attributes"]["slug"] == potion_name:
                    potion_effect = i["attributes"]["effect"]
                else:
                    continue
            
                return potion_effect
            
            except:
                return f"The {potion_name} you submitted was not found in the database"


if __name__ == "__main__":
    main()