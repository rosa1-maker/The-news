import unittest
from .models import News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the News class
    '''


    def setUp(self):
        '''
        set up method that will run before every Test
        '''
        self.new_news = News()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

