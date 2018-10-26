# -*- coding:utf-8 -*-
import unittest
import subprocess
import os,sys
class TestMain(unittest.TestCase):



    def test_main(self):
        path = __file__
        path = sys.path[0]
        ppath = os.path.dirname(path)
        mainPath = os.path.join(ppath,"main.py")
        testFolder = path

        cmds = [
                    "python",
                    mainPath,
                    "-f",
                    testFolder
                ]
        subprocess.call(cmds)