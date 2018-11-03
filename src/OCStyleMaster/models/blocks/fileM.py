# -*- coding:utf-8 -*-

import os
from OCStyleMaster.models.blocks.base import *

class FileM(File):

    def __init__(self, filePath):
        super(FileM, self).__init__(filePath)



    def analyze(self):
        for child in self.children:
            child.analyze()





