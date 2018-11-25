# -*- coding:utf-8 -*-
import unittest
import subprocess
import os,sys


class TestMain(unittest.TestCase):



    def test_main(self):
        path = __file__
        ppath = os.path.dirname(path)
        pppaath = os.path.dirname(ppath)
        mainPath = os.path.join(pppaath,"main.py")
        testFolder = ppath

        cmds = [
                    "python",
                    mainPath,
                    "-f",
                    testFolder
                ]
        subprocess.call(cmds)