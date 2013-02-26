import logging
import os


class Logger():
    
    def __init__(self, news):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self._fileDirectoryPath = './'
        self._fileDirectory = 'logs'
        self.checkDirectoryExist(self._fileDirectoryPath+self._fileDirectory)
        self._fileHandler = logging.FileHandler(self._fileDirectoryPath+self._fileDirectory+'/'+news+'.log')
        self._formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self._fileHandler.setFormatter(self._formatter)
        self.logger.addHandler(self._fileHandler)
        
    def checkDirectoryExist(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        
    def get(self):
        return self.logger