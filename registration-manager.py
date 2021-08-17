#!/usr/bin/python
import csv 
import tabulate

raw_data = open("battle_royale.csv", "r")
address = csv.reader(raw_data)
data_list = list(address)

def prompt_print():
    # options
    print("\n" + "*"*20 + "MAIN MENU" + "*"*20 + "\n")
    print("\ta: Find pre-registered player")
    print("\tb: Find the number of a specific player")
    print("\tc: Print list of players")
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

def number_to_player():
    index = int(input("What player number do you need to find? > "))
    print(data_list[index])


def player_to_number():
    print("Search for a player name! (NYI)")
    query = str(input("What name do you want to look for? > "))
    print(list(address))

def main():
    try: 
        print("\nWelcome to the Battle Royale Game Tournament Registration!")
        prompt_print()
        choice = get_abc()
        if choice == "a":
            number_to_player()
        if choice == "b":
            player_to_number()
        if choice == "c":
            print(tabulate.tabulate(address, headers="firstrow"))
            print("Bye!")
    except KeyboardInterrupt:
        print("\nBye!")

main()
