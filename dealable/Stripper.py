from bs4 import BeautifulSoup

class Stripper:
    
    def __init__(self):        
        pass
    
    def strip(self, html):
        return (''.join(BeautifulSoup(html).findAll(text=True))).strip()