import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    '''English to French testing'''
    def test_enfr(self):
        # Test Hello returns Bonjour
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # Test Hello does not return Hello
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
    def test_fren(self):
        # Test Bonjour returns Hello
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        #Test Hello does not return Hello
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

unittest.main()


    
     
