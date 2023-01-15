## Map Layout
mapdict = {
    "A": {
        "up": None,
        "down": "C",
        "left": None,
        "right": "B",
    },
    "B": {
        "up": None,
        "down": "D",
        "left": "A",
        "right": None,
    },
    "C": {
        "up": "A",
        "down": None,
        "left": None,
        "right": "D",
    },
    "D": {
        "up": "B",
        "down": None,
        "left": "C",
        "right": None,
    },
}


def move_room(cur_room):
    direction = input("Leaving " + cur_room + ". Enter direction: ").lower()
    while direction not in mapdict[cur_room] or mapdict[cur_room][direction] is None:
        print("Invalid direction. You are in room " + cur_room)
        direction = input("Leaving " + cur_room + ". Enter direction: ").lower()
    
    print("You are in room " + mapdict[cur_room][direction])
    return mapdict[cur_room][direction]



items = {
    "A": ["chest", "key"],
    "B": ["amulet", "matches"],
    "C": ["statue", "diary"],
    "D": ["potion", "crowbar"],
    "inventory": [],
}


def inter_item(cur_room):
    print ("Room " + cur_room + " contains " + str(items[cur_room]))
    action = input("Select an item ").lower()
    while action not in items[cur_room]:
        print('"' + action + '"' + " is not in this room.")
        action = input("Select an item ").lower()

    items[cur_room].remove(action)
    items["inventory"].append(action)
    print ("Room " + cur_room + " contains" + str(items[cur_room]) 
    + " and your inventory contains " + str(items['inventory']))
        

location = "A"

while True:
    choice = input("Leave " + str(location) + " or search? ").lower()
    if choice == "leave":
        location = move_room(location)
    elif choice == "search":
        inter_item(location)
    else:
        print("Invalid command.")
