# Welcome to Jessica's ePortfolio :smile:



## Professional self-assessment:

Completing my coursework throughout the program and developing the ePortfolio has helped to showcase my strengths by able to apply everything I learned in the program. I was able to use some of my knowledge to design, develop, and test my code for my program. Completing my coursework throughout the program and developing the ePortfolio shape my professional goals and values to prepare me to enter or become more employable in the computer science field by helping me apply problem solving skills to get any general problem statement into precise algorithmic solutions. The program also helped me become proficient in my programming language with helping when looking for employment in the computer science field. I also learned to apply the computational and algorithmic problem-solving skills. When I took the course Object Orient Analysis/Design, I got to design using flowchart and UML. Creating the UML model help in show the relationship and programming ideas. When I took the course collaboration and team project, we were able to collaborate in a team environment and problem-solve things as a team. We got to review each other code and give each other feedback. These feedbacks helped me improve my coding skills and learn from my mistakes. I also provided feedback to my peers to help them improve any errors that were made and helpful tips. Using communication in any course throughout my program and in the real world is very important. Being able to communicate to stakeholders can help you receive information on their needs and can help impact the success of the project. Having communication with the stakeholders can help minimums the risk of your projects. Data structures are used to arrange the data in the computer memory or disk storage and algorithm searches and sort the data. In one of my programs that I developed; the user was able to make a choice on what they want to do in the ATM. Once the user picked a choice, the user was able to either view their balance, withdraw money, deposit money, and exit. For software engineering, I was able to develop few programs. I developed a Tic Tac Toe game, so the user was able to versus the computer. I also developed the ATM program that I mentioned above. To develop these programs, I first brainstorm any ideas and then designed it by making a flow chart. In my previous course, I used UML for requirements and making sure it will meet those requirements. I then developed a basic program and test it over and over until achieving my requirements. In the database, I developed some python, SQL, MongoDB, and MySQL programs that let the user create, read, update, and delete (CRUD) data from the database. For security, I got to learn a lot about security threats, malware, and hackers. I learned how to prevent these in different ways like antivirus programs, encryption, firewall, and so on.  

My artifacts fit together and inform the portfolio as a whole by showing what I have learned over the past few months in SNHU. The first artifact in software engineering, I was able to first get the program that I created from my pervious course and convert it from Java to python. I first had to brainstorm to make sure that I made the code run like how my previous had it by using another programming language. Then I develop the program and was testing different part of the code to make sure if it was functioning correctly. For the next artifact, I did a program in data structures and algorithms. I was able to develop a program in python to make a game called Tic Tac Toe. The data structures and algorithms in this game was able to let the user versus the computer and let the user place the letter that they chose in the row and column that they picked. The computer is generated to using random spot to place the letter, rows and columns that are not chosen by the user. The artifact that I developed for databases was a simple CRUD program that can collect and store data. This database allows the user to create, read, update, and delete items. The user can pretty much use this as list of anything they want. The user can then be able to come back to the database to update and/or read the items in the list. If the user ever decides to delete any items in the list, they are able to. I created a code review video, to help analyze the previous program that I created. This helps me review each line of my code and see if there any improvement in the code I made. It also helps detect any errors and if I need to add any comments that is needed. All these artifacts show my abilities to develop using different programming languages, problem-solving skills, analytical skills, creativity and also help with my critical thinking. 



## Code Review: 

**Below is the link to my code review video:**




## Software Engineering/ Design:

  The artifact that I chose is a previous existing code that I did in my previous course. I used Java to implement the fundamental operations of create, read, update, and delete (CRUD) using MongoDB driver to access my document collection. For this existing code, I had to create a document in MongoDB database called “city” into the collection “inspections.” Then I developed a function to be able to read that document and also to be able to update the document when needed. I also developed a function to delete any document that I no longer needed. 
  
  I selected this code because I want to test my skills and abilities by being able to transfer this existing code into a different language like python. When transferring my existing code into python, I work on the project piece by piece and tested it each time. I think I met some of the objectives that I planned to meet with this enhancement. I think being able to work on my CRUD functionally but using a different language was a good way to enhance my skills since this can help me improve my skills in different programming languages and not just one. Being able to improve my workflow of my program and debugging it can help with my outcome. 
  
 The challenges that I had when transferring the existing code to python is trying to make the program run smoothly. I had to do a lot of debugging and look at any syntax errors that I might have created when writing the code. I learned to do the code piece by piece and testing it instead of doing it all at once. This could of help me find any errors I made instead of going through each line to find out what I did wrong. I kept everything the same since I got a positive feedback.  
 


**Below is the code that I created:**

```
import json
from bson import json_util
from pymongo import MongoClient

def main():
connection = MongoClient('localhost', 27017)
db = client.City
mydb = db.Inspection
print('Here is list of information:')
counter = 0
for item in mydb.find():
  counter = counter + 1
  old_name = str(item['name'])
  old_description = str(item['description'])
  print("name:" + item['name'] + 'description:'+item['description'])
  choice1 = input('Please enter choice 1 to update 2 to delete record')
  while not choice1.isdigit() or int(choice1) > 2 or int(choice1)< 1:
    choice1 = input('Invalid choice. Please enter correct one')
    if counter == 0:
      print('There is no recorded to update...')
      return
    if int(choice1) is 1:
      print('Please enter key to update ')
      choice = input('1. for name 2. for description')
      while not choice.isdigit() or int(choice) > 2 or int(choice) < 1:
        choice = input('Invalid choice. Please enter correct one')
        if int(choice) is 1:
          value = input('Enter new name:')
          old_value = old_name
          
          else:
            value = input('new description')
            old_value = old_description
            update_record(mydb, choice, value, old_value)
            else:
              name = input('Please enter name to remove from database:')
              while not name:
                name = input('Invalid imput. Please enter correct name')
                remove_record(mydb, name)
              
                
                def update_record(mydb, choice, value, old_value):
                  if int(choice) is 1:
                    query_update = {"name": old_value}
                    new_value = {"$set": {"name": value}}
                    else:
                      query_update = {"description": old_value}
                      new_value = {"$set":{"description": value}}
                      mydb.update_one(query_update, new_value)
                      print("data successfully inserted...")
                      
                      def remove_record(mydb, name):
                        query_del = {"name": name}
                        mydb.delete_one(query_del)
                        print('data successfully deleted...')
                        
                        main()
```








## Data Structure and Algorithms:

  The artifact that I chose for data structures and algorithm is tic tac toe. I created this half of this game for fun two months ago and finished it this week. I created this game using the programming language python. In this game, the player versus the computer using a board that was created with strings. The player has a choice to choose if they want to be X or if they want to be O. The board is printed on the terminal and randomly choose which player goes first. Once the player is picked to go first, choose a number 1 through 9 to place their letter. The computer then randomly chose a spot that is free. A message will be displayed if the computer wins or in the user wins. 
	
  I picked this because it shows the data structures and algorithms that is used in this game. In the game tuple was used for X and O by using indexes. The string is also used throughout the code to help create the board and to display messages to the user. The letters that are used in the game also used String. Algorithms are used to get user input and the output. The input help get the letter the user use to play the game and also the number that they picked when placing the letter on the spot that is picked. This artifact was half done when I first created it. I finished working on it and tested it to make sure it was working correctly. I did some adjusting on some area that wasn’t working. I think objectives that I planned to meet with the enhancement did get met. I was able to use linear search in the game to move the letter on the board by using the number that the user picked. The binary search that I think was the letters that were in the index. I don’t think I have any updates to my outcome coverage plans at this moment. I learned that more about algorithms when creating this game. The challenges that I had was to know where to use the search algorithms. Also, make sure my loop was working correctly or written correctly was a bit of a challenge. I kept everything the same since I got a positive feedback. 
  


**Below is the code for Tic Tac Toe:**

```
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
```






## Database:

For this artifact, I chose to make a python program. I created a simple program where the user can create, read, update, and delete items. The user can start by create a new register. The user then will be able to read the insert they made. The user can also be able to update the item that is on the list. The program will then display the user the update before and the update after it been made. The update can be removing item from the list or adding new one. The user can also be able to delete everything on the list.

I selected this because this artifact collects data, and generally stores it. It let the user have control on the item they chose to add in their list. Being able to use the CRUD method to help me made this program showcase my skills and abilities. I was able to do a simple program that can store data into the database and get used when needed. I think objectives that I planned to meet with the enhancement did get met. I was able to store the data that the user typed in and let the user have control on the data usage. I don’t think I have any updates to my outcome coverage plans at this moment. The challenges were making sure that my program was working correctly and making sure I did it accurately. I kept everything the same since I got a positive feedback. 



**Below is the code for my CRUD database:**


```
#!/usr/bin/python
from pymongo import *

class MongoDB_Supplies:
    def __init__(self):
      
        # Initialize the connection 
 self.connection = MongoClient('localhost', 27017)
        self.db = self.connection.Items       
        self.cursor = self.db.Storage 
        
    def create(self, query={}):
        # Insert a new register.
        self.cursor.insert(query)
        
    def read(self, query={}):
        # Read all the register.
        for value in self.cursor.find(query):
            print(value)
        
    def update(self, query_1={}, query_2={}):
        
        # Be able to change the first item on the list.
        self.cursor.update(query_1, query_2)
    
    def delete(self):
        
        # Delete all on the list.
        for i in self.cursor.find():
            self.cursor.remove(i)

if __name__ == '__main__':
    mongo = MongoDB_Supplies()

    for x in range(3):
        reg = {'_id': x, 'x': x, 'list':['first', 'second', 'third','fourth', 'fifth']}
        mongo.create(reg)
        
    print('Before update: ')
    mongo.read()
    
    mongo.update({'x':0, 'list':'first'}, {'$set':{'list.$':'primeiro'}})
    
    # Add a new item on the list.
    mongo.update({'x':1}, {"$addToSet":{'list':{'$each':['fifth', 'sixth', 'seventh']}}})
    
    # Remove one item on the list.
    mongo.update({'x':2}, {'$pull':{'list':'fifth'}})
    
    print('After update: ')
    mongo.read()
    
    mongo.delete()
```
