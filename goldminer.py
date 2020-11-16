class Miner:
    x = 0
    y = 0
    front = 0
    
    def scan(self, board):
        print("Scan method")
        
    def rotate(self):
        front += 90
        
        if front >= 360:
            front = 0
    
    def move(self, board):
        print("Move method")
 
 
class Board:
    def __init__(self, length):
        self.length = length
        self.table = [["-" for x in range(length)] for y in range(length)]
        self.table[0][0] = "M"
        
    def addSet(self, set, symbol):
        for i in range(len(set)):
            self.table[set[i][0]][set[i][1]] = symbol
            
    def print(self):
        print()
        for i in range(self.length):
            for j in range(self.length):
                print(self.table[i][j], end=' ')
            print()
        print()
 
#Main func
length = int(input("Enter size of grid: "))
 
miner = Miner()
board = Board(length)
 
board.print()
 
print("--Gold--")
goldX = int(input("Enter x-location of gold: "))
goldY = int(input("Enter y-location of gold: "))
 
gold = [[goldX, goldY]]
board.addSet(gold, "G")
board.print()
 
print("--Beacons--")
numBeac = int(input("Number of beacons: "))
beacon = [[0 for x in range(2)] for y in range(numBeac)]
for i in range(numBeac):
 beacon[i][0] = int(input("X-location of Beacon " + str(i+1) + ": "))
 beacon[i][1] = int(input("Y-location of Beacon " + str(i+1) + ": "))
 print()
 
board.addSet(beacon, "B")
board.print()
 
print("--Pits--")
numPit = int(input("Number of pits: "))
pit = [[0 for x in range(2)] for y in range(numPit)]
for i in range(numPit):
 pit[i][0] = int(input("X-location of Pit " + str(i+1) + ": "))
 pit[i][1] = int(input("Y-location of Pit " + str(i+1) + ": "))
 print()
 
board.addSet(pit, "P")
board.print()
 
print("Rest of the program")