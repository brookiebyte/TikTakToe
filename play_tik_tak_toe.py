# Libraries

# Global Variables
isXTurn = True
grid = "_1_|_2_|_3_\n_4_|_5_|_6_\n 7 | 8 | 9 "

# Functions

def SwitchTurns():
    global isXTurn
    if isXTurn == True:
        print("X")
        isXTurn = False
    else:
        print("O")
        isXTurn = True

def ConvertGridToIndex(gridSpace):
    if gridSpace == 1:
        indexElement = 1
    if gridSpace == 2:
        indexElement = 5
    if gridSpace == 3:
        indexElement = 9
    if gridSpace == 4:
        indexElement = 13
    if gridSpace == 5:
        indexElement = 17
    if gridSpace == 6:
        indexElement = 21
    if gridSpace == 7:
        indexElement = 25
    if gridSpace == 8:
        indexElement = 29
    if gridSpace == 9:
        indexElement = 33
    return indexElement
   
#print(grid[33])

# Main
print(grid)
while True:
   print(input())
   print("is it X's turn?: " + str(isXTurn))
   SwitchTurns()




