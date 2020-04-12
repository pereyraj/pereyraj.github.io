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