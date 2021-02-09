import random

def boardType(opponentType):
    board = {}
    if opponentType == "Computer" or opponentType == "computer":
        board = {1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 :"X", 6 : 6, 7 : 7, 8 : 8, 9 : 9}
    elif opponentType == "PvP" or opponentType == "pvp" or opponentType =="PVP":
        board = {1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 : 9}
    return board

def StartGame():
    print("\n" * 100)
    opponentType = input("Do you want to face a computer or local PvP? (Computer or PvP)")
    board = boardType(opponentType)
    GameStateCheckEnemy(board, opponentType)

def DisplayBoard(board):
    print("\n" * 98)
    board = board
    b1, b2, b3, b4, b5, b6, b7, b8, b9 = board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8], board[9]
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", b1, "  |  ", b2, "  |  ", b3, "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", b4, "  |  ", b5, "  |  ", b6, "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", b7, "  |  ", b8, "  |  ", b9, "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    
def UserInput(board, opponentType):
    startingChar = ""
    while True:
        if opponentType == "PvP" or opponentType == "pvp" or opponentType =="PVP":
            startingChar = "X"
        elif opponentType == "Computer" or opponentType == "computer":
            startingChar = "O"
        else:
            print("Invalid Input: Please try again")
            UserInput(board, opponentType)
        print("Player", startingChar)
        userInput = int(input("Please select a number that is on the board: "))
        if userInput > 0 and userInput < 10:
            if board[userInput] != "X" and board[userInput] != "O":
                board[userInput] = startingChar
                DisplayBoard(board)
                break
            else:
                print("Invalid Input: Please try again")
                UserInput(board, opponentType)
        else:
            print("Invalid Input: Please try again")
            UserInput(board, opponentType)
            break
    GameStateCheckUser(board, opponentType)
        
def EOGPrompt():
    restartInput = str(input("Do you wish to continue?"))
    print("\n" * 100)
    if restartInput == "Yes" or restartInput == "yes" or  restartInput == "y" or  restartInput == "Y" or  restartInput == "YES" or restartInput == "YEs" or  restartInput == "YeS":
        StartGame()
    elif restartInput == "No" or restartInput == "no":
        print(exit)
        exit()
    else:
        print("Invalid Selection")
        EOGPrompt()


def statecheck(board): 
    keysList = []
    List = []
    for keys, values in board.items():
        keysList.append(keys)
        List.append(values)
    movesLeft = tilecheck(List)
    gameState = Check(List)
    if gameState == "X":
        print("X Wins!")
        EOGPrompt()
    elif gameState == "O":
        print("O Wins!")
        EOGPrompt()
    elif movesLeft == 0:
        print("Tie Game!")
        EOGPrompt()
    else:
        print("Game has up to", movesLeft, "moves left!")       
        
            
def GameStateCheckUser(board, opponentType):
    DisplayBoard(board)
    statecheck(board)
    OpponentMove(board, opponentType)


def GameStateCheckEnemy(board, opponentType):
    DisplayBoard(board)
    statecheck(board)
    UserInput(board, opponentType)    


def tilecheck(List): #Also checks how many spaces are avaliable
    count = 0
    while count < 8:
        count = 0
        for elem in List:
            if elem == 1:
                count += 1
            elif elem == 2:
                count += 1
            elif elem == 3:
                count += 1
            elif elem == 4:
                count += 1
            elif elem == 5:
                count += 1
            elif elem == 6:
                count += 1
            elif elem == 7:
                count += 1
            elif elem == 8:
                count += 1
            elif elem == 9:
                count += 1
                break
            elif elem == "X" or elem == "O":
                count = count
            else:
                count = 0
                break
        return count


def Check(List):
    charTuple = ("X", "O")
    for elem in charTuple:
        if List[0] == elem and List[1] == elem and List[2] == elem:
            gamestate = elem
            return gamestate
        elif List[3] == elem and List[4] == elem and List[5] == elem:
            gamestate = elem
            return gamestate
        elif List[6] == elem and List[7] == elem and List[8] == elem:
            gamestate = elem
            return gamestate
        elif List[0] == elem and List[3] == elem and List[6] == elem:
            gamestate = elem
            return gamestate
        elif List[1] == elem and List[4] == elem and List[7] == elem:
            gamestate = elem
            return gamestate
        elif List[2] == elem and List[5] == elem and List[8] == elem:
            gamestate = elem
            return gamestate
        elif List[0] == elem and List[4] == elem and List[8] == elem:
            gamestate = elem
            return gamestate
        elif List[2] == elem and List[4] == elem and List[6] == elem:
            gamestate = elem
            return gamestate
        else:
            continue
        
        
def OpponentMove(board, opponentType):
    enemyInput = ""
    enemyChar = ""
    if opponentType == "PvP" or opponentType == "pvp" or opponentType =="PVP":
        enemyChar = "O"
    elif opponentType == "Computer" or opponentType == "computer":
        enemyChar = "X"
    if opponentType == "PvP" or opponentType == "pvp" or opponentType =="PVP":
        print("Player", enemyChar)
        enemyInput = int(input("Please select a number that is on the board: "))
    elif opponentType == "Computer" or opponentType == "computer":
        enemyInput = random.randrange(1, 10)
    else:
        print("Invalid Input: Please try again")
        OpponentMove(board, opponentType)
    if board[enemyInput] != "X" and board[enemyInput] != "O":
        print(board[enemyInput])
        board[enemyInput] = enemyChar
        GameStateCheckEnemy(board, opponentType)
    else:
        print("Invalid Input: Please try again")
        OpponentMove(board, opponentType)


StartGame()