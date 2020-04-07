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
          