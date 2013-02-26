import unittest

from dealable.deals import GrouponMy

class TestDealSource(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def grouponMy(self):
        deal = GrouponMy()
        deal.scrapSource('all')
        
if __name__ == '__main__':
    #unittest.main()
    tests = ['grouponMy']
    testClass = TestDealSource
    suite = unittest.TestSuite(map(testClass, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)