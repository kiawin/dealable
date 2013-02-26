from dealable.deals import Deal

class GrouponMy(Deal):
    '''
    Scraper Class: Groupon Malaysia
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self._deal = 'grouponMy'
        super().__init__(self._deal)
        
        self.default_url_prefix = 'http://www.groupon.my/'
        self.append_url_prefix = False
        self.default_source_expression = ['div.deal-content p.deal-title a']
        self.sources = {
                        'all': {
                                'url': 'http://alldeals.groupon.my/',
                                'tags': ['groupon','malaysia'],
                                'source_expr': self.default_source_expression,
                                'url_prefix': self.default_url_prefix
                                }
                        }

    def sanitize(self, text):
        '''
        Sanitize text
        '''
        return " ".join(text.split()).replace('\u2018','\'').replace('\u2019','\'')

        
    def __del__(self):
        pass