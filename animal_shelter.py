#Example Python Code to Insert a Document
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username,password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:28190/?authMechanism=DEFAULT&authSource=AAC'%(username,password))
        self.database = self.client['AAC']

    # Complete this create method to implement the C in CRUD.
    def create(self, animal_data):
        if animal_data is not None:
            self.database.animals.insert_one(animal_data)  # data should be dictionary
        else:
            raise Exception("Failed to add Data")
        

		 # used to find an animal from the db given some few characteristics
    def read(self, criteria):
        if criteria is not None:
            data = self.database.animals.find(criteria)  # data should be dictionary 
            for document in data:

                return document
        else:
            raise Exception("nothing to read, hint is empty")
            
    # used to get all the animals in the collection
    def read_all(self, criteria):
        if criteria is not None:
            data = self.database.animals.find(criteria) # dat should be dictionary 
            # for document in data:
            return [self.stringify_id(i) for i in data]
        else:
            raise Exception("nothing to read, hint is empty")
            
            
        # used to get all the dogs that meet the criteria or perferences that is selected by the user
    def read_preferred_dogs(self, criteria):
        if criteria is not None:
            data = self.database.animals.find(criteria) # dat should be dictionary 
            # for document in data:
            return [self.stringify_id(i) for i in data]
        else:
            raise Exception("nothing to read, hint is empty")

		# this method cast the _id ObjectId to String. this was done to avoid the error during rendering on the table     
    def stringify_id(self,animal):
        animal["_id"] = str(animal["_id"])
        return animal    


    # this method is used to delete animal from the db
    def delete(self, _animal):
        if _animal is not None:
            data = self.read(_animal) # find animal first
            if data is None:
                print("Animal does not exist")
                return
            self.database.animals.delete_many(_animal)  # data should be dictionary 
        else:
            raise Exception("nothing to delete, animal data is empty")
            
    # used for updating animal
    def update(self, _criteria,_newData):
        if _criteria is not None and _newData is not None:
            self.database.animals.update_many(_criteria,{'$set':_newData}) 
            self.read(_criteria)
            
        else:
            raise Exception("please enter both key and data to modify the collection")





