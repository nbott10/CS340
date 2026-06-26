# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

def __init__(self, user, pwd):
   username=user
   password=pwd
   host='localhost'
   port=27017
   database= AAC'
   collection='animals'
   auth='admin'

    self.client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/{database}?authSource={auth}")
    self.database = self.client['%s' % database]
    self.collection = self.database['%s' % collection]

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            self.database.animals.insert_one(data)  # data should be dictionary             
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    def read_all(self,query):
        if query is not None:
            try:
                cursor = self.collection.find(query)
                documents = list(cursor)
                return documents
            except PyMongoError as e:
                print(f"An error occured trying to find documents: {e}")
                return[]
            else:
                raise Exception("Query Empty")
                
    #Updated method for U in CRUD
    def update(self, query, new_data):
        try:
            result = self.collection.update_many(query, {'$set' : new_data})
            return result.modified_count
        except Exception as e:
            print(f"error: {e}")
            return 0
        
    #Delete method for D in CRUD
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"error : {e}")
            return 0
    
        
        