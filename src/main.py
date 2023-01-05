mapdict = {
    "A": {
        "up": None,
        "down": "E",
        "left": None,
        "right": "B",
    },
    "B": {
        "up": None,
        "down": "F",
        "left": "A",
        "right": None,
    },
    "E": {
        "up": "A",
        "down": None,
        "left": None,
        "right": "F",
    },
    "F": {
        "up": "B",
        "down": None,
        "left": "E",
        "right": None,
    },
}
location = "A"
while True:
    direction = input("Enter direction:").lower()
    if direction == "quit" : break
    if direction in mapdict[location] and mapdict[location][direction] is not None:
        location = mapdict[location][direction]
    else:
        print("Invalid direction")
    print("You are in room " + location)