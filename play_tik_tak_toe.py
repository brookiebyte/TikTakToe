# Libraries

# Global Variables
isXTurn = True

# Functions

def PrintEmptyBoard():
    print("___|___|___")
    print("___|___|___")
    print("   |   |   ")

def SwitchTurns():
    global isXTurn
    isXTurn = not isXTurn

# Main

PrintEmptyBoard() 
while True:
   print(input())
   print("is it X's turn?: " + str(isXTurn))
   SwitchTurns()
