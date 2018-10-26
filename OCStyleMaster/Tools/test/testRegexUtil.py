# -*- coding:utf-8 -*-


import unittest
from Tools import *
import sys
import os
class TestRegexUtil(unittest.TestCase):

    def tearDown(self):
        # 每个测试用例执行之后做操作
        pass

    def setUp(self):

        pass


    def test_func_regex(self):
        path = os.path.abspath(".")
        path += "/oc.m"
        f = open(path,"r")
        text = f.read()
        ret =  RegexUtil.find_all_func_declare(text)
        print(len(ret))
        print(ret)




    def test_func_line_count(self):
        text = "123\n123\n\nbbb\n"
        ret = RegexUtil.line_count(text)
        self.assertEqual(ret,4)

    def test_func_empty_line_count(self):
        text = "123\n123\n\nbbb\n\n"
        ret = RegexUtil.empty_line_count(text)
        self.assertEqual(ret, 2)