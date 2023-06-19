import math
import random

roomNames = ["Garden", "Prison", "Garrison", "Field"]
poCon = ["north", "east", "south", "west"]
width = int(input("What is the longest the dungeon should be? (3 - 15)"))
size = width**2
map = []
for i in range(width):
    map.append([])
buildQueue = []
firstX = width
firstY = width
lastX = 0
lastY = 0

for y in range(len(map)):
    for x in range(len(map)):
        map[y].append(None)




class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
"""
print(f"{bcolors.OKGREEN}{bcolors.BOLD}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

"""
class room:
    #Class Properties
    name = "" 
    doors = []
    connectedDoors = []
    lock = None
    items = []
    disToCore = 0
    x = 0
    y = 0
    visited = False
    active = False
    generation = 1


    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"
    
    def trim(self, cuts):
        for i in cuts:
            self.remove(i)
    
    def rolecall(self):
        print(self)
        for i in self.children:
            print()
            print(i)


def addCon(roo, *dir):
    global size

    count = random.randint(1, 4 - roo.generation)
    if count <= 1:
        rem = random.sample(poCon, count)
    else:
        rem = dir
    size -= count
    for i in rem:
        roo.doors.append(i)


def adjBuilder(source):   #Build Adjacent Rooms
    global size
    if "north" in source.doors and source.y > 0:
        source.connectedDoors.append('north')
        build(source.x, source.y-1, "south", source.generation + 1)
    elif "north" in source.doors:
        source.doors.remove("north")
    if "east" in source.doors and source.x < 8:
        source.connectedDoors.append('east')
        build(source.x+1, source.y, "west", source.generation + 1)
    elif "east" in source.doors:
        source.doors.remove("east")
    if "south" in source.doors and source.y < 8:
        source.connectedDoors.append('south')
        build(source.x, source.y+1, "north", source.generation + 1)
    elif "south" in source.doors:
        source.doors.remove("south")
    if "west" in source.doors and source.x > 0:
        source.connectedDoors.append('west')
        build(source.x-1, source.y, "east", source.generation + 1)
    elif "west" in source.doors:
        source.doors.remove("west")
    
def build(x, y, dir, gen):     #Build Room to the North
    global size
    if map[y][x] != None:
        return
    newRoom = room(random.sample(roomNames, 1)[0])
    addCon(newRoom, dir)
    if dir not in newRoom.doors:
        newRoom.doors.append(dir)
        size-= 1
    newRoom.x = x
    newRoom.y = y
    newRoom.generation = gen
    map[newRoom.y][newRoom.x] = newRoom
    buildQueue.append([newRoom.y, newRoom.x])

def mapTrim():
    global firstX, firstY, lastX, lastY
    for row, y in enumerate(map):
        for col, x in enumerate(y):
            if x != None:
                if col > lastX:
                    lastX = col
                if row > lastY:
                    lastY = row
                if col < firstX:
                    firstX = col
                if row < firstY:
                    firstY = row
            



def printMap(current):
    for rowNum, y in enumerate(map):
        for colNum, x in enumerate(y):
            if colNum >= firstX and colNum <= lastX and rowNum >= firstY and rowNum <= lastY:
                if x != None:
                    name = str(x.name).center(10," ")
                    if x == current:
                        print(f"{bcolors.OKGREEN}{name}{bcolors.ENDC}", end=" ")
                    elif x.visited:
                        print(bcolors.OKCYAN + name + bcolors.ENDC, end = " ")
                    else:
                        print(bcolors.WARNING + "Unknown".center(10, " ") + bcolors.ENDC, end=" ")
                else:
                    print(f"{bcolors.FAIL}" + "X".center(10," ") + bcolors.ENDC, end=" ")
        if rowNum >= firstY and rowNum <= lastY:
            print()


core = room("Core Room")
core.x = int(len(map)/2)
core.y = int(len(map)/2)
core.visited = True
map[core.y][core.x] = core
cd = random.sample(poCon, random.randint(3, 4))
for i in cd:
    core.doors.append(i)
    size -= 1
size -= 1
#addCon(core)

print(f"{core}")
print(core.doors)


adjBuilder(core)

for dorl in buildQueue:
    adjBuilder(map[dorl[0]][dorl[1]])
    buildQueue.remove(dorl)
    if size < 0:
        break

mapTrim()
# firstX = 0
# firstY = 0
# lastX = len(map)
# lastY = lastX
printMap(core)
playerX = core.x
playerY = core.y
#remCon(core)
#print(core.doors)

def move(dir):
    global playerX, playerY
    cur = map[playerY][playerX]
    if dir == 'u' or dir == 'up' or dir == 'n' or dir == 'north':
        if 'north' in cur.connectedDoors and cur.lock != 'north':
            playerY -= 1
        elif cur.lock == 'north':
            print("The way is blocked.")
        else:
            print("You cannot go that way.")

    elif dir == 'r' or dir == 'right' or dir == 'e' or dir == 'east':
        if 'east' in cur.connectedDoors  and cur.lock != 'east':
            playerX += 1
        elif cur.lock == 'east':
            print("The way is blocked.")
        else:
            print("You cannot go that way.")

    elif dir == 'd' or dir == 'down' or dir == 's' or dir == 'south':
        if 'south' in cur.connectedDoors  and cur.lock != 'south':
            playerY += 1
        elif cur.lock == 'south':
            print("The way is blocked.")
        else:
            print("You cannot go that way.")

    elif dir == 'l' or dir == 'left' or dir == 'w' or dir == 'west':
        if 'west' in cur.connectedDoors  and cur.lock != 'west':
            playerX -= 1
        elif cur.lock == 'west':
            print("The way is blocked.")
        else:
            print("You cannot go that way.")
    
    else:
        print("That is not a valid direction.")

    
    cur = map[playerY][playerX]
    cur.visited = True
    printMap(cur)

lastInput = ''

while lastInput != "stop" and lastInput != "end":
    lastInput = input("What do you do? ").lower()
    inputList = lastInput.split()
    inLen = len(inputList)

    if inLen >= 2:
        if inputList[0] == 'go' or inputList[0] == 'move':
            move(inputList[1])
            print(f"({playerX}, {playerY})")

    if inLen == 1:
        if lastInput == "map":
            printMap(map[playerY][playerX])
    