#!/usr/bin/python
import csv 
import tabulate

raw_data = open("battle_royale.csv", "r")
address = csv.reader(raw_data)

def prompt_print():
    # options
    print("\n" + "*"*20 + "MAIN MENU" + "*"*20 + "\n")
    print("\ta: Player ID --> Player Summary")
    print("\tb: Player Search")
    print("\tc: List players")
    print("\tCtrl-c exits at any point.")


def get_abc():
    try: 
        choice = str(input("\t > "))
        return choice
    except ValueError: 
        print("Please enter either A, B or C.")
        return get_abc()
    if choice not in ("a", "b", "c"): # thanks @isagalev@mastodon.social
        print("Please enter either a, b or c. (try a lowercase!)")
        return get_abc()

def number_to_player(): # option A
    index = int(input("What player number do you need to find? > "))
    #print(list(address)[index])
    print("\n" + tabulate.tabulate(
        [["Avatar Name", "Player Name", "Player Number"],
        list(address)[index]], 
        headers="firstrow") + "\n\nBye!")


def player_to_number(): # option B
    query = str(input("\nWhat name do you want to look for? > "))
    matches = [["Avatar Name", "Player Name", "Player Number"]]
    for line in address:
        for entry in line: 
            if entry.lower().find(query.lower()) > 0:
                matches.append(line)
                
    if matches == [["Avatar Name", "Player Name", "Player Number"]]:
        print("No matches found, try again!")
    else: 
        print("\n" + tabulate.tabulate(matches, headers="firstrow") + "\nBye!")


def main():
    try: 
        print("\nWelcome to the Battle Royale Game Tournament Registration!")
        prompt_print()
        choice = get_abc()
        if choice == "a":
            try: 
                number_to_player()
            except IndexError:
                print("Please enter a number between 1 and 50.")
                number_to_player()
        if choice == "b":
            player_to_number()
        if choice == "c":
            print(tabulate.tabulate(address, headers="firstrow"))
            print("Bye!")
    except KeyboardInterrupt:
        print("\nBye!")

main()
