import unittest
from utils import *

class TestRegexUtil(unittest.TestCase):

    def test_is_comment_line(self):

        text = " // adcbd"
        ret = RegexUtil.is_comment_line(text)
        self.assertEqual(ret, True)

    def test_is_comment_line1(self):

        text = " abd //adcbd"
        ret = RegexUtil.is_comment_line(text)
        self.assertEqual(ret, False)

    def test_is_comment_line2(self):
        text = "// Uncomment the following line to display an Edit button in the navigation bar for this view controller."
        ret = RegexUtil.is_comment_line(text)
        self.assertEqual(ret, False)

