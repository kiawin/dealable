from dealable import Scraper
from dealable import Logger
from dealable import Stripper

from dealable import Source

from pymongo.errors import OperationFailure

class Deal():
    '''
    Deal Scraper Class
    '''
    
    def __init__(self, deals):
        '''
        Constructor
        '''
        #self.logger = Logger(deals).get()
        
        self.default_database = 'deals'
        self.default_collection = deals
        self.default_url_prefix = None
        self.append_url_prefix = False
        self.default_deal_expression = None
        
        self.sources = {}
    
    def sanitize(self, text):
        '''
        Sanitize text (Abstract method)
        '''
        return text
    
    def scrapSource(self, category, multi=False):
        '''
        Save all deal urls from one category into collection
        '''
        
        source = Source(self.default_database, self.default_collection)
        count = {'total': 0, 'scraped': 0}
        details = self.sources[category]
        
        scraper = Scraper(details['url'])
        scrap = scraper.get()
        
        for source_expr in details['source_expr']:
            
            #For Temporal - Testing only
            allItems = scrap.select(source_expr)
            print('size: '+str(len(allItems)))
            
            for item in allItems:
                count['total'] += 1
                print('Deal: '+str(count['total']))
                title = self.sanitize(str(item.contents[0]))
                print(title)
                url = str(item['href'])
                print(url)
                print()
                
                tags = details['tags']
                
                source.addSource(url, title, category, tags)
                
                try:
                    source.insertSources()
                    count['scraped'] += 1
                except OperationFailure as of:
                    #self.logger.error("Skipped - " + str(of))
                    pass
                finally:
                    source.resetSources()
        if multi is False:
            info = "Total Items scraped: " + str(count['scraped']) + '/' + str(count['total'])
            #self.logger.info(info)
            print(info)
        else:
            return count



