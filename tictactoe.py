from os import system
import random

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

blankBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []
level = 0

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    #system('cls')
    print("Tic Tac Toe - Artificial Intelligence edition\n")
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('- + - + -')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('- + - + -')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print("")

def numOfWins(board, enemy):
    numWins = 0
    if not (enemy in {board['7'], board['8'], board['9']}): # across the top
        numWins = numWins + 1
    if not (enemy in {board['4'], board['5'], board['6']}): # across the middle
        numWins = numWins + 1
    if not (enemy in {board['1'], board['2'], board['3']}): # across the bottom
        numWins = numWins + 1
    if not (enemy in {board['1'], board['4'], board['7']}): # down the left side
        numWins = numWins + 1
    if not (enemy in {board['2'], board['5'], board['8']}): # down the middle
        numWins = numWins + 1
    if not (enemy in {board['3'], board['6'], board['9']}): # down the right side
        numWins = numWins + 1
    if not (enemy in {board['7'], board['5'], board['3']}): # diagonal
        numWins = numWins + 1
    if not (enemy in {board['1'], board['5'], board['9']}): # diagonal
        numWins = numWins + 1
    
    #printBoard(board)
    #print(numWins, "   enemy: ", enemy)
    return numWins

def winChecker(board):
    if board['7'] == board['8'] == board['9'] != ' ': # across the top
        return True
    elif board['4'] == board['5'] == board['6'] != ' ': # across the middle
        return True
    elif board['1'] == board['2'] == board['3'] != ' ': # across the bottom
        return True
    elif board['1'] == board['4'] == board['7'] != ' ': # down the left side
        return True
    elif board['2'] == board['5'] == board['8'] != ' ': # down the middle
        return True
    elif board['3'] == board['6'] == board['9'] != ' ': # down the right side
        return True
    elif board['7'] == board['5'] == board['3'] != ' ': # diagonal
        return True
    elif board['1'] == board['5'] == board['9'] != ' ': # diagonal
        return True
    else:
        return False

def game(opponentTurn):
    system('clear')
    print("Welcome to Tic Tac Toe - Artificial Intelligence edition\n")
    print('7' + ' | ' + '8' + ' | ' + '9')
    print('- + - + -')
    print('4' + ' | ' + '5' + ' | ' + '6')
    print('- + - + -')
    print('1' + ' | ' + '2' + ' | ' + '3')
    level = int(input("\nChoose Difficulty Level (0,1,2): "))

    turn = 'X'
    count = 0
    theBoard = blankBoard.copy()

    for i in range(9):
        printBoard(theBoard)
        if opponentTurn == True:
            print("It's the opponent's turn")
            opponentTurn = False
            if level == 0:
                move = str(random.randint(1, 9))
                while theBoard[move] != ' ':
                    move = str(random.randint(1, 9))

            elif level == 1:
                if turn == 'X':
                    enemy = 'O'
                else:
                    enemy = 'X'
                if count == 0:
                    move = "5"
                elif count == 2:
                    if theBoard["9"] == enemy or theBoard["1"] == enemy:
                        move = "7"
                    else:
                        move = "9"
                elif count == 4:
                    found = False
                    for i in range(1,10):
                        futureBoard = theBoard.copy()
                        if futureBoard[str(i)] == ' ':
                            futureBoard[str(i)] = turn
                            if winChecker(futureBoard) == True:
                                move = str(i)
                                found = True
                                break
                    if found == False:
                        for i in range(1,10):
                            futureBoard = theBoard.copy()
                            if futureBoard[str(i)] == ' ':
                                futureBoard[str(i)] = enemy
                                if winChecker(futureBoard) == True:
                                    move = str(i)
                                    found = True
                                    break
                    if found == False:
                        for i in range(1, 10):
                            if futureBoard[str(i)] == ' ':
                                for j in range(i+1, 10):
                                    futureBoard = theBoard.copy()
                                    if futureBoard[str(j)] == ' ':
                                        futureBoard[str(i)] = turn
                                        futureBoard[str(j)] = turn
                                        if winChecker(futureBoard) == True:
                                            move = str(i)
                                            found = True
                                            break
                            if found == True:
                                break
                    
                elif count == 6:
                    found = False
                    for i in range(1,10):
                        futureBoard = theBoard.copy()
                        if futureBoard[str(i)] == ' ':
                            futureBoard[str(i)] = turn
                            if winChecker(futureBoard) == True:
                                move = str(i)
                                found = True
                                break
                    if found == False:
                        for i in range(1,10):
                            futureBoard = theBoard.copy()
                            if futureBoard[str(i)] == ' ':
                                futureBoard[str(i)] = enemy
                                if winChecker(futureBoard) == True:
                                    move = str(i)
                                    found = True
                                    break
                    if found == False:
                        move = str(random.randint(1, 9))
                        while theBoard[move] != ' ':
                            move = str(random.randint(1, 9))
                elif count == 8:
                    move = str(random.randint(1, 9))
                    while theBoard[move] != ' ':
                        move = str(random.randint(1, 9))
                elif count == 1:
                    if theBoard["5"] == ' ':
                        move = "5"
                    else:
                        move = "9"
                elif count == 3:
                    found = False
                    for i in range(1,10):
                        futureBoard = theBoard.copy()
                        if futureBoard[str(i)] == ' ':
                            futureBoard[str(i)] = enemy
                            if winChecker(futureBoard) == True:
                                move = str(i)
                                found = True
                                break
                    if found == False:
                        if theBoard["9"] == ' ':
                            move = "9"
                        else:
                            move = "7"
                elif count == 5:
                    found = False
                    for i in range(1,10):
                        futureBoard = theBoard.copy()
                        if futureBoard[str(i)] == ' ':
                            futureBoard[str(i)] = turn
                            if winChecker(futureBoard) == True:
                                move = str(i)
                                found = True
                                break
                    if found == False:
                        for i in range(1,10):
                            futureBoard = theBoard.copy()
                            if futureBoard[str(i)] == ' ':
                                futureBoard[str(i)] = enemy
                                if winChecker(futureBoard) == True:
                                    move = str(i)
                                    found = True
                                    break
                    if found == False:
                        for i in range(1, 10):
                            if futureBoard[str(i)] == ' ':
                                for j in range(i+1, 10):
                                    futureBoard = theBoard.copy()
                                    if futureBoard[str(j)] == ' ':
                                        futureBoard[str(i)] = turn
                                        futureBoard[str(j)] = turn
                                        if winChecker(futureBoard) == True:
                                            move = str(i)
                                            found = True
                                            break
                            if found == True:
                                break
                elif count == 7:
                    found = False
                    for i in range(1,10):
                        futureBoard = theBoard.copy()
                        if futureBoard[str(i)] == ' ':
                            futureBoard[str(i)] = turn
                            if winChecker(futureBoard) == True:
                                move = str(i)
                                found = True
                                break
                    if found == False:
                        for i in range(1,10):
                            futureBoard = theBoard.copy()
                            if futureBoard[str(i)] == ' ':
                                futureBoard[str(i)] = enemy
                                if winChecker(futureBoard) == True:
                                    move = str(i)
                                    found = True
                                    break
                    move = str(random.randint(1, 9))
                    while theBoard[move] != ' ':
                        move = str(random.randint(1, 9))

            elif level == 2:
                highest = -99
                if turn == 'X':
                    enemy = 'O'
                else:
                    enemy = 'X'
                
                for i in range(1, 10):
                    futureBoard = theBoard.copy()
                    if futureBoard[str(i)] == ' ':
                        futureBoard[str(i)] = turn
                        #printBoard(futureBoard)
                        if winChecker(futureBoard) == True:
                            eval = 100
                        else:
                            eval = numOfWins(futureBoard, enemy) - numOfWins(futureBoard, turn)
                        #print("eval: ", eval, "  i: ")
                        if eval > highest:
                            highest = eval
                            move = str(i)

            theBoard[move] = turn
        
        else:
            print("It's your turn -- Move to which place?")
            valid = False
            
            opponentTurn = True
            
            while valid == False:
                move = input("move> ")

                if theBoard[move] == ' ':
                    theBoard[move] = turn
                    valid = True
                else:
                    print("That place is already filled.\nMove to a valid place...")  

        count += 1
        

        if count >= 5:
            if winChecker(theBoard) == True: # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" ** " + turn + " won. **")
                break

        if count == 9:
            printBoard(theBoard)
            print("\nGame Over.\n")
            print("It's a Tie!!")
            
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

if __name__ == "__main__":
    move = "Y"
    opponentFirst = False
    while move == "Y" or move == "y":
        game(opponentFirst)
        move = input("Do you want to play again? : ")
        opponentFirst = not opponentFirst