#!/usr/bin/python
import csv 

raw_data = open("battle_royale.csv", "r")
address = csv.reader(raw_data)


def prompt():
    # options
    print("\n\n" + "*"*20 + "MAIN MENU" + "*"*20)
    print("\tA: Find pre-registered player")
    print("\tB: Find the number of a specific player")
    print("\tC: Print list of players")
    print("\tDo ^C (Ctrl c) at any time to exit.")
    return input("\t > ").lower()


def number_to_player():
    print("Enter a number (NYI)")
    return 0


def player_to_number():
    print("Search for a player name! (NYI)")
    return 0


def print_players():
    for line in address:
        print(line)


def main():
    print("Welcome to the Battle Royale Game Tournament Registration!")
    try: 
        choice = prompt()
        if choice == 'a':
            number_to_player()
        if choice == 'b':
            player_to_number()
        if choice == 'c':
            print_players()
    except KeyboardInterrupt:
        print("\nBye!")

main()
