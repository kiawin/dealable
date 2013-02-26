from datetime import datetime
from dealable import MongoDB

class Item(MongoDB):
    def __init__(self, dbname='test', colname='posts'):
        '''
        Constructor for Item
        '''
        self.dbname = dbname
        self.colname = colname
        super().__init__(self.dbname, self.colname)
        ''' Instance variables '''
        self.item = {}
    
    def addItem(self, url, price, facts, content):
        self.item['url'] = url
        self.item['price'] = price
        self.item['facts'] = facts
        self.item['content'] = content
    
    def insertItem(self):
        modified = datetime.now()
        r = super().set({
                         "url": self.newsItem['url']
                         },
                        {
                         "content": str(self.newsItem['content']),
                         "modified": modified
                         })
        return r
    
    def resetNewsItem(self):
        self.newsItem = {}