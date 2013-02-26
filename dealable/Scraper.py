from bs4 import BeautifulSoup
import urllib.request

class Scraper():
    
    def __init__(self, url):
        '''
        Constructor for Scraper
        '''
        self._url = url
        self._headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)', "Content-Type": "charset=utf-8"}
        self._req = urllib.request.Request(self._url, None, self._headers)
        self._html = urllib.request.urlopen(self._req).read()
        self._soup = BeautifulSoup(self._html, 'lxml')
    
    def get(self):
        '''
        Return Scraper Object
        '''
        return self._soup
    
    def __del__(self):
        self._req = None
        self._html = None
        self._soup = None