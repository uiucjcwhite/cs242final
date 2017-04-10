__author__ = 'Cameron'
import unittest
from src.scraper import scraper_utilities as su

class Test_Utilities(unittest.TestCase):

    def test_clean_strings(self):
        """
        Tests the clean string utility function.
        Implicitly tests the rest of the string utility functions
        :return:
        """
        self.assertEqual("Jeff Bezos", su.clean_string("Jeff Bezos [4]"))
        self.assertEqual("Jeff Bezos", su.clean_string('Jeff Bezos [4][5]'))
        self.assertEqual("Jeff Bezos", su.clean_string('Jeff Bezos')) #No Change expected
        self.assertEqual("Jeff Bezos", su.clean_string('Jeff Bezos\n\n\n'))
        self.assertEqual("Jeff Bezos", su.clean_string('Jeff' + u'\xa0' + 'Bezos'))
