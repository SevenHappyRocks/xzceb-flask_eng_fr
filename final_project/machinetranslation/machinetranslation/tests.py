import unittest

from translator import english_To_French, french_To_English

class Testfrench_To_English(unittest.TestCase):
    def test1(self):
        self.assertIsNone(english_To_French(None))
        self.assertEqual(french_To_English('Bonjour'), 'Hello')
        self.assertEqual(french_To_English('door'), 'porte')
        self.assertEqual(french_To_English('Fromage'), 'Cheese')
        self.assertNotEqual(french_To_English('quelle'), 'Bye')

class Testenglish_To_French(unittest.TestCase):
    def test1(self):
        self.assertIsNone(french_To_English(None))
        self.assertEqual(english_To_French('Hello'), 'Bonjour')
        self.assertEqual(english_To_French('Full'), 'plein')  
        self.assertNotEqual(english_To_French('Turkey'), 'Burrito') 


unittest.main()  
