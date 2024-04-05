import random


# making a random choice chooser between wow and rust. 

# SOD phase 3 released today, Best Force Wipe update was released today in recent timing.

# i wanna play both but i lack the time. 

def choice(x, y):
    randomChoice = random.choice([x, y])
    randomTask = random.choice(["dungeon-grind", "quest"])
    randomServer = random.choice(["Reddit", "Rustified", "Rusticated", "Rustoria", "Rusty Moose"])

    if randomChoice == 'rust':
        print("Rust")
        if randomServer == "Reddit":
            return "Reddit"
        elif randomServer == "Rustified":
            return "Rustified"
        elif randomServer == "Rusticated":
            return "Rusticated"
        elif randomServer == "Rustoria":
            return "Rustoria"
        elif randomServer == "Rusty Moose":
            return "Rusty Moose"
    elif randomChoice == 'wow':
        print("WoW")
        if randomTask == "dungeon-grind":
            return "Dungeon-Grind"
        else:
            return "Questing"

print(choice("rust", "wow"))




