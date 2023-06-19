startX = 4
startY = 4
lastInput = ""
moveCheck = 0
goldKeyLost = 0
#map = [[0,   1,  2,  3,  4],
#       [5,   6,  7,  8,  9],
#       [10, 11, 12, 13, 14],
#       [15, 16, 17, 18, 19],
#       [20, 21, 22, 23, 24]]

       #Location Names for tracking location
loc = ["The Garden",      "The Mossy Wall",  "The Slick Steps", "The Patio",   "The Treeline", 
       "The Compost Bin", "The Lounge West", "The Lounge East", "The Kitchen", "Dining Room North",
       "Guest Bedroom",   "Hallway",         "Master Bedroom",  "Pantry",      "Dining Room Middle",
       "Laundry Room",    "Garage",          "Mudroom",         "Foyer",       "Dining Room South",
       "Sidewalk",        "Driveway",        "Sidewalk",        "Road",        "Road"]

lockDoorStat = "LOCKED"
garDoorStat = "CLOSED"
       #Location Descriptions
desc = ["The flowers are bloomming by the fence to the North and West", "The wall to the South is covered in moss, the fence to the North seems fine though.", "The steps are slick and you almost slip, luckily no one is looking through the window to the South.", "Standing at the railing, there is a beautiful view view to the North.", "The dark woods beyond the treeline are too firghtening, you want to go back West.", 
            "There is nothing here but a bin of food scraps and worms, time to go back North.", "The West side of the Lounge has a nice chair facing the Kitchen, and a Hallway to th South", "The East side of the Lounge has a large modern TV, with an old grandfather clock beside it.", "There is meat thawing on the counter, with spice jars around it.", "The North end of a long Dining Room, there are to place settings at the head of the table.",
            "The Guest Bedroom must be an after thought, just a bunch of books and pictures with a bed crammed in where if fits.", f"A short hallway connecting the Lounge to the Guest and Master Bedrooms and a {lockDoorStat} door to the Garage", "A large bed sits at the far wall, with pictures hung around the room, a vanity sits in the corner.", "The pantry is stocked with jars of jams and jellies.", "You can see the wood out the window, a nearby tree's branch taps at the glass.",
            "The Laundry Room is very quiet with nothing being cleaned.", f"An old truck sits on the west side of the Garage, an oil puddle sits to the east, the garage door is {garDoorStat}.", "The mudroom holds a few pairs of muddy boots and a nice pair of dress shoes.", "An awkward room by the Mudroom, that struggles to be called a Foyer.", "The South End of a very long Dining Room.",
            "A small walkway heading past the side of the house, there's not much here.", "The Driveway heading up to the garage, a car has dripped oil, staining part of it.", "The trees part and you can see a house, there's a door just to the North.", "The road continues, to the West you see a paved path alongside the gravel.", "You find yourself lookng at a locked gate to the East, with a fence to the North and South."]

        #Location Movement Restrctions, using % with various prime numbers to track which directions have walls in the way
        #Multiples of 2 cannot move North, 3 East, 5 South, and 7 West
restr = [["east", "south"],                       #Garden
        ["east", "west"],                         #Mossy Wall
        ["east", "west"],                         #Slick Steps
        ["east", "south", "west"],                #Porch
        ["west"],                                 #Tree Line
        ["north"],                                #Compost
        ["east", "south"],                        #Lounge West
        ["east", "west"],                         #Lounge East
        ["north", "east", "south", "west"],       #Kitchen
        ["south", "west"],                        #Dining North
        ["east"],                                 #Guest Bedroom
        ["north"],                                #Hallway
        ["west"],                                 #Master Bedroom
        ["north"],                                #Pantry
        ["north", "south"],                       #Dining Mid
        ["east"],                                 #Laundry
        ["east", "west"],                         #Garage
        ["east", "west"],                         #Mudroom
        ["east", "south", "west"],                #Foyer
        ["north", "west"],                        #Dining South
        ["east"],                                 #Sidewalk end
        ["east", "west"],                         #Driveway
        ["east", "west"],                         #Door
        ["east", "west"],                         #Road
        ["west"]                                  #Gate
        ]

itemLoc = [[],[],[],[],["stick"], 
           [],[],[],[],["food scraps"], 
           ["dirty clothes"],[],["gate key"],[],[], 
           [],[],[],[],[], 
           ["bronze key"],[],[],[],[]]

inventory = []

def help():
    print("Map - Print a map showing your position as an X.")
    print("Look - Look around for any items laying around.")
    print("Grab - Grab a nearby item.")
    print("Inventory/Inv - List the items you've picked up.")
    print("Use <number> - Use the item at the numbered position in your inventory.")
    print("Go/Move <direction> - Use to move along a cardinal direction, so long as there's nothing in your way.")

def refDesc(entry):
    if entry == 11:
        desc[entry] = f"A short hallway connecting the Lounge to the Guest and Master Bedrooms and a {lockDoorStat} door to the Garage"
    if entry == 16:
        desc[entry] = f"An old truck sits on the west side of the Garage, an oil puddle sits to the east, the garage door is {garDoorStat}. A door to the north is {lockDoorStat}."

def printMap(x, y):
    for yi in range(5):
        for xi in range(5):
            if yi == 4 and xi > 0:
                if yi == y and xi == x:
                    print("[  x  ]", end = " ")
                else:
                    print("[     ]", end = " ")
            elif xi == x and yi == y:
                print("[x]", end = " ")
            else:
                print("[ ]", end = " ")
        print()
myX = startX
myY = startY

print("Welcome to the game! Use 'HELP' if you need instructions.")




print(desc[myY * 5 + myX])

while lastInput != "stop" and lastInput != "end":

    
    pastLoc = myY * 5 + myX
    lastInput = input("What do you do? ").lower()
    moveCheck = 0 #Movement check to prevent spammed 'There is a wall there'
    inputStart = lastInput.split()

    if inputStart[0] == "help":
        help()

    if lastInput == "map": #prints a basic map, after adding walls this won't be as useful
        printMap(myX, myY)
    
    if inputStart[0] == "look":
        if len(itemLoc[pastLoc]) != 0:
            print(f"There is a {itemLoc[pastLoc][0]}")
        else:
            print("There's nothing around.")
        if pastLoc ==14 or pastLoc == 19 and len(itemLoc[9]) != 0:
            print("You see two place settings at the North end of the table.")
        elif pastLoc == 21 and len(itemLoc[20]) != 0:
            print("You see something glittering at the end of the path to the West.")

    if inputStart[0] == "grab":
        if len(itemLoc[pastLoc]) != 0:
            print(f"You grabbed the {itemLoc[pastLoc][0]}")
            inventory.append(itemLoc[pastLoc][0])
            itemLoc[pastLoc].remove(inventory[len(inventory)-1])
        else:
            print("There's nothing to grab.")

    if inputStart[0] == "inventory" or inputStart[0] == "inv":
        for index, i in enumerate(inventory):
            print(f"{index+1}: {i}")

    if pastLoc == 11 and inputStart[0] == "unlock":
        lockDoorStat = "unlocked"
        refDesc(11)
        restr[11].append("south")
        restr[16].append("north")

    if pastLoc == 16 and inputStart[0] == "open":
        garDoorStat = "open"
        refDesc(16)
        restr[16].append("south")
        restr[21].append("north")

    if inputStart[0] == "cheat":
        inventory.append("gate key")


    if len(inputStart) > 1:
        if inputStart[0] == "go" or inputStart [0] == "move":
            if inputStart[1] in restr[pastLoc]:
                if inputStart[1] == "north":
                    if pastLoc == 22:
                        myX+=1
                    myY-=1
                elif inputStart[1] == "east":
                    myX+=1
                elif inputStart[1] == "south":
                    if pastLoc == 18:
                        myX-=1
                    myY+=1
                elif inputStart[1] == "west":
                    myX-=1
                printMap(myX, myY)
            else:
                print("You cannot go that way.")
        if inputStart[1].isnumeric():
            numb = int(inputStart[1]) - 1
            if inputStart[0] == "use" and numb < len(inventory) and numb > -1:
                if inventory[numb] == "bronze key" and pastLoc == 22:
                    print("You use the Bronze Key to unlock the front door.")
                    restr[22].append("north")
                    restr[18].append("south")
                    inventory.remove("bronze key")

                elif inventory[numb] == "food scraps" and pastLoc == 5:
                    print("You toss the food scraps into the compost bin, this would make excellent fertilizer.")
                    itemLoc[pastLoc].append("fertilizer")
                    inventory.remove("food scraps")

                elif inventory[numb] == "fertilizer" and pastLoc == 0:
                    print("You sprinkle fertilizer about the plants, a carrot looks about ready to harvest.")
                    itemLoc[pastLoc].append("carrot")
                    inventory.remove("fertilizer")
                    
                elif inventory[numb] == "carrot" and pastLoc == 8:
                    print("You cook a tasty meal with meat and veggies, ready to serve!")
                    itemLoc[pastLoc].append("meal")
                    inventory.remove("carrot")

                elif inventory[numb] == "meal" and pastLoc == 9:
                    print("You sit down and eat, once you've finished you notice a silver key where the spoon should've been.")
                    itemLoc[pastLoc].append("silver key")
                    inventory.remove("meal")

                elif inventory[numb] == "silver key" and pastLoc == 11:
                    print("You fit the silver key into the lock on the guest bedroom to the west.")
                    restr[11].append("west")
                    restr[10].append("east")
                    inventory.remove("silver key")

                elif inventory[numb] == "gold key" and pastLoc == 11:
                    print("You fit the gold key into the lock on the master bedroom to the east.")
                    restr[12].append("west")
                    restr[11].append("east")
                    inventory.remove("gold key")

                elif inventory[numb] == "dirty clothes" and pastLoc == 15:
                    print("You load the laundry into the washer and wait. As you moved the clothes into the dryer, something golden fell out of a pocket and below the dryer.")
                    inventory.remove("dirty clothes")
                    goldKeyLost = 1

                elif inventory[numb] == "stick" and pastLoc == 15 and goldKeyLost == 1:
                    print("You use the stick to reach under the drier and pull out a golden key.")
                    goldKeyLost = 2
                    itemLoc[pastLoc].append("gold key")

                elif inventory[numb] == "gate key" and pastLoc == 24:
                    print("You unlock the gate and are free to go!")
                    inventory.remove("gate key")
                    lastInput = "stop"

            elif inputStart[0] == "use":
                print("You can't use what you don't have.")



    if inputStart[0] == "movement":
        print(restr[pastLoc])










    """
    if (inputStart[0] == "go" or inputStart[0] == "move") and len(inputStart) > 1:

        if inputStart[1] == "north" and (restr[myY][myX] % 2 != 0 or restr[myY][myX] == 0):
            myY -= 1
            print("You walk North.")
            moveCheck = 1
        elif moveCheck == 0:
            moveCheck = -1

        if inputStart[1] == "south" and (restr[myY][myX] % 5 != 0 or restr[myY][myX] == 0):
            myY += 1
            print("You walk South.")
            moveCheck = 1
        elif moveCheck == 0:
            moveCheck = -1

        if inputStart[1] == "west" and (restr[myY][myX] % 7 != 0 or restr[myY][myX] == 0):
            myX -= 1
            print("You walk West.")
            moveCheck = 1
        elif moveCheck == 0:
            moveCheck = -1

        if inputStart[1] == "east" and (restr[myY][myX] % 3 != 0 or restr[myY][myX] == 0):
            myX += 1
            print("You walk East.")
            moveCheck = 1
        elif moveCheck == 0:
            moveCheck = -1

        if moveCheck == -1:
            print("There is a wall there.")
            moveCheck = 0


            """

    currentLoc = myY * 5 + myX




    if currentLoc != pastLoc:
        print(desc[myY * 5 + myX])
    



    #Debug output comment out before submitting!!    
    #print(f"You are at {loc[myY * 5 + myX]}")
    #print(f"{currentLoc}")




