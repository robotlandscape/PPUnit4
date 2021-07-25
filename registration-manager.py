import csv 

def init():
    raw_data = open("battle_royale.csv", "r")
    address = csv.reader(raw_data)

def prompt():
    # options
    print("\n\n" + "*"*20 + "MAIN MENU" + "*"*20)
    print("\tA: Find pre-registered player")
    print("\tB: Find the number of a specific player")
    print("\tC: Print list of players")
    print("\tQ: Quit/Log Out")

    
    return input("\t > ").lower()

def main():
    print("Welcome to the Battle Royale Game Tournament Registration!")
    init()
    choice = prompt()
    print(choice)

main()
