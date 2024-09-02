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


# Main
print(grid)
while True:
   print(input())
   print("is it X's turn?: " + str(isXTurn))
   SwitchTurns()




