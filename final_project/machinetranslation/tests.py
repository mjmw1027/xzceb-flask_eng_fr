import unittest

from translator import english_to_french,french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('None'),'')
        self.assertEqual(french_to_english('0'),'Hello')

class TestEnglishToFrench(unittest.TestCase):
    def test2(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')


unittest.main()
