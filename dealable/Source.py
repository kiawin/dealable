from datetime import datetime
from dealable import MongoDB

class Source(MongoDB):
    def __init__(self, dbname='test', colname='posts'):
        '''
        Constructor for Source
        '''
        self.dbname = dbname
        self.colname = colname
        super().__init__(self.dbname, self.colname)
        ''' Instance variables '''
        self.items = []
        
    def addSource(self, url, title, category, tags):
        '''
        Append source to instance variable
        '''
        modified = created = datetime.now()
        item = {'url': url, 'title': title, 'category': category, 'tags': tags, 'created': created, 'modified': modified}
        self.items.append(item)
        
    def insertSources(self):
        '''
        Insert source(s) into DB
        '''
        #if len(self.items) is not 0:
        #    print(str(self.items))
        r = super().insert(self.items)
        return r
    
    def resetSources(self):
        self.items = []