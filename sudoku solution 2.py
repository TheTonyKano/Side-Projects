def inputBoard():
    # Should Output Yes
    #board = [
    #    "295743861",
    #    "431865927",
    #    "876192543",
    #    "387459216",
    #    "612387495",
    #    "549216738",
    #    "763524189",
    #    "928671354",
    #    "154938672"]
    
    # Should Output No
    #board = [
    #    "195743862",
    #    "431865927",
    #    "876192543",
    #    "387459216",
    #    "612387495",
    #    "549216738",
    #    "763524189",
    #    "928671354",
    #    "254938671"]
    
    # To input line by line manually
    board = []
    for i in range(1, 10):
        line = input("Enter line "+ str(i) +" :")
        if len(line) == 9:   
            board.append(line)
        else:
            print("Incorrect entry, please check lines has values between 1 and 9")
    
    boardmatrix = [[number for number in value] for value in board]
    if grids3x3(boardmatrix) == True: 
        if rows(boardmatrix) == True:
            if columns(boardmatrix) == True: 
                print("Yes")
    else:
        print("No")


def rows(board):
    return verifyNumbers(board)


def verifyNumbers(lst):
    if [False for i in range(9) for n in range(1,10) if str(n) not in lst[i]] == False:
        return False
    else:
        return True


def columns(board):
    return verifyNumbers([[value[c] for value in board] for c in range(9)])


def grids3x3(board):
    blocks = [board[x+a][y+b]for y in (0, 3, 6) for x in (0, 3, 6) for b in (0, 1, 2) for a in (0, 1, 2)]
    gridlist = [blocks[i * 9:(i + 1) * 9] for i in range((len(blocks)+ 9 - 1)// 9)]
    for i in range(9):
        for n in range(1,10):
            if str(n) not in gridlist[i]:
                return False
            else:
                continue
    return True



inputBoard()