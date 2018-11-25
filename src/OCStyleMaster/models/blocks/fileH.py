# -*- coding:utf-8 -*-


import os
from OCStyleMaster.globalData import *
from OCStyleMaster.models.blocks.base import *


class FileH(File):

    def __init__(self, filePath):
        super(FileH, self).__init__(filePath)



    def analyze(self):
        """
        分析主函数
        :return:
        """
        for child in self.children:
            child.analyze()




