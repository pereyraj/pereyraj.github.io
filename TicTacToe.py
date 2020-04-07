# Tic Tac Toe
 
import random

def drawBoard(board):
    # This function prints out the board.

    print('    |    |')
    print(' ' + board[1] + '  | ' + board[2] + '  | ' + board[3])
    print('    |    |')
    print('---------------')
    print('    |    |')
    print(' ' + board[4] + '  | ' + board[5] + '  | ' + board[6])
    print('    |    |')
    print('---------------')
    print('    |    |')
    print(' ' + board[7] + '  | ' + board[8] + '  | ' + board[9])
    print('    |    |')
 
def inputPlayerLetter():
    # Lets the player type which letter they want to be.

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('\nChoose if you want to be X or O?')
        letter = input().upper()
 
    # the first element in the tuple is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
 
def whoGoesFirst():
    # This randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
 
def playAgain():
    # This function returns True if the player wants to play again, if not then it returns.
    print('\nDo you want to play again? (yes or no)')
    return input().lower().startswith('y')
 
def makeMove(board, letter, move):
    board[move] = letter
 
def isWinner(board, letter):
    # This function returns True if that player has won.
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or 
    (board[4] == letter and board[5] == letter and board[6] == letter) or 
    (board[1] == letter and board[2] == letter and board[3] == letter) or 
    (board[7] == letter and board[4] == letter and board[1] == letter) or 
    (board[8] == letter and board[5] == letter and board[2] == letter) or 
    (board[9] == letter and board[6] == letter and board[3] == letter) or 
    (board[7] == letter and board[5] == letter and board[3] == letter) or 
    (board[9] == letter and board[5] == letter and board[1] == letter))   
 
def getBoardCopy(board):
    # Make a duplicate of the board list and return it.
    dupeBoard = []
 
    for i in board:
        dupeBoard.append(i)
 
    return dupeBoard
 
def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '
 
def getPlayerMove(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not spaceFree(board, int(move)):
        print('Pick your next move? (1-9)')
        move = input()
    return int(move)
 
def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if spaceFree(board, i):
            possibleMoves.append(i)
 
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
 
def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
 
    # Algorithm:
    # Move letter if player can win
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if spaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
 
    # Block player letter if player could win
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if spaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
 
    # Try to take one of the corners if available.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
 
    # Try to take the center if available.
    if spaceFree(board, 5):
        return 5
 
    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
 
def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if spaceFree(board, i):
            return False
    return True
    

print('Tic Tac Toe!')


while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('\nThe ' + turn + ' was picked to go first.')
    gameIsPlaying = True
 
    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
 
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You won!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Tie!')
                    break
                else:
                    turn = 'computer'
 
        else:
            # Computer's turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
 
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer wins! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Tie!')
                    break
                else:
                    turn = 'player'
 
    if not playAgain():
        break