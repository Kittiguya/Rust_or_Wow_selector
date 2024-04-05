import random


# making a random choice chooser between wow and rust. 

# SOD phase 3 released today, Best Rust Force Wipe update was released today in recent timing.

# i wanna play both but i lack the time. 

def choice(x, y):
    randomChoice = random.choice([x, y])
    randomTask = random.choice(["dungeon-grind", "quest"])
    randomServer = random.choice(["Reddit", "Rustified", "Rusticated", "Rustoria", "Rusty Moose"])

    match randomChoice:
        case "rust":
            print("Rust")
            match randomServer:
                case "Reddit":
                    return "Reddit"
                case "Rustified":
                        return "Rustified"
                case "Rusticated":
                        return "Rusticated"
                case "Rustoria":
                        return "Rustoria"
                case "Rusty Moose":
                        return "Rusty Moose"
            
        case "wow":
            print("wow")
            match randomTask:
                case "dungeon-grind":
                    return "Dungeon-Grind"
                case "quest":
                    return "Quest"


print(choice("rust", "wow"))




