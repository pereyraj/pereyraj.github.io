# Welcome to Jessica's ePortfolio

My name is Jessica Pereyra. I live in New Hampsire. My major is Computer Science and I am a student at Southern New Hampshire University. I have a 10 years old son name Jayden and two dogs. In my free time, I like to spend time with family and friends. 

This site was created to showcase some of my work in coding. 


## Code Review 

## Software Engineering/ Design

  The artifact that I chose is a previous existing code that I did in my previous course. I used Java to implement the fundamental operations of create, read, update, and delete (CRUD) using MongoDB driver to access my document collection. For this existing code, I had to create a document in MongoDB database called “city” into the collection “inspections.” Then I developed a function to be able to read that document and also to be able to update the document when needed. I also developed a function to delete any document that I no longer needed. 
  
  I selected this code because I want to test my skills and abilities by being able to transfer this existing code into a different language like python. When transferring my existing code into python, I work on the project piece by piece and tested it each time. I think I met some of the objectives that I planned to meet with this enhancement. I think being able to work on my CRUD functionally but using a different language was a good way to enhance my skills since this can help me improve my skills in different programming languages and not just one. Being able to improve my workflow of my program and debugging it can help with my outcome. 
  
 The challenges that I had when transferring the existing code to python is trying to make the program run smoothly. I had to do a lot of debugging and look at any syntax errors that I might have created when writing the code. I learned to do the code piece by piece and testing it instead of doing it all at once. This could of help me find any errors I made instead of going through each line to find out what I did wrong. 
 
 **Below is the link to the code:**

[https://github.com/pereyraj/pereyraj.github.io/blob/master/enhancement.py](url)


**Code:**


`import json
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
          old_value = old_name ' `
          
         ` else:
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
                        
                        main()  `

## Data Structure and Algorithms

  The artifact that I chose for data structures and algorithm is tic tac toe. I created this half of this game for fun two months ago and finished it this week. I created this game using the programming language python. In this game, the player versus the computer using a board that was created with strings. The player has a choice to choose if they want to be X or if they want to be O. The board is printed on the terminal and randomly choose which player goes first. Once the player is picked to go first, choose a number 1 through 9 to place their letter. The computer then randomly chose a spot that is free. A message will be displayed if the computer wins or in the user wins. 
	
  I picked this because it shows the data structures and algorithms that is used in this game. In the game tuple was used for X and O by using indexes. The string is also used throughout the code to help create the board and to display messages to the user. The letters that are used in the game also used String. Algorithms are used to get user input and the output. The input help get the letter the user use to play the game and also the number that they picked when placing the letter on the spot that is picked. This artifact was half done when I first created it. I finished working on it and tested it to make sure it was working correctly. I did some adjusting on some area that wasn’t working. I think objectives that I planned to meet with the enhancement did get met. I was able to use linear search in the game to move the letter on the board by using the number that the user picked. The binary search that I think was the letters that were in the index. I don’t think I have any updates to my outcome coverage plans at this moment. I learned that more about algorithms when creating this game. The challenges that I had was to know where to use the search algorithms. Also, make sure my loop was working correctly or written correctly was a bit of a challenge.
  
**Below is the link to the code:**

[https://github.com/pereyraj/pereyraj.github.io/blob/master/TicTacToe.py](url)

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/pereyraj/pereyraj.github.io/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
