import unittest

from dealable.DB import MongoDB

class TestDealUniqueUrl(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def grouponMy(self):
        '''
        Set url field as unique
        '''
        db = MongoDB('deals', 'grouponMy')
        db.setUnique('url')
        db.__del__()

if __name__ == '__main__':
    #unittest.main()
    tests = ['grouponMy']
    testClass = TestDealUniqueUrl
    suite = unittest.TestSuite(map(testClass, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)