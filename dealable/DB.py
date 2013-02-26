from pymongo import MongoClient


class MongoDB():
    def __init__(self, dbname='test', colname = 'posts'):
        self.database = None
        self.collection = None
        self.connection = None
        
        self._dbname = dbname
        self._colname = colname
        self.__connect()
        
    def __connect(self):
        self.connection = MongoClient()
        self.database = self.connection[self._dbname]
        self.collection = self.database[self._colname]
    
    def getConnection(self):
        return self.connection
    
    def getCollection(self):
        return self.collection
    
    def getDatabase(self):
        return self.database
    
    def insert(self, docs = None):
        return self.collection.insert(docs)

    def update(self, query = None, modifier = None):
        return self.collection.set(query, modifier)
    
    def set(self, query = None, modifier = None):
        return self.collection.update(query, {"$set": modifier})
    
    def unset(self, query = None, modifier = None):
        return self.collection.update(query, {"$unset": modifier})
    
    def inc(self, query = None, modifier = None):
        return self.collection.update(query, {"$inc": modifier})
    
    def rename(self, query = None, modifier = None):
        return self.collection.update(query, {"$rename": modifier})
    
    def findOne(self, query = None):
        return self.collection.find_one(query)
    
    def find(self, query = None):
        return self.collection.find(query)
    
    def setUnique(self, key):
        return self.collection.ensure_index(key,unique=True)
    
    #def __str__(self):
    #    return '\n'.join(map(str,self.newsItems))
    
    def __del__(self):
        self.connection.close()