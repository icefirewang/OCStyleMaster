# -*- coding:utf-8 -*-

import unittest


class FuncTest(unittest.TestCase):

    def test_regex(self):
        text = "012345678901"
        regex = "01"
        m = RegexUtil.full_search(regex,text)
        print(m)
        pass