# -*- coding:utf-8 -*-

from .blockBase import *
from utils import *
import os

class FileM(BlockBase):

    def __init__(self, filePath):

        self.path = filePath
        f = open(self.path,"r")
        self.text =  f.read()

        _ , ext = os.path.splitext(self.path)
        self.ext = ext
        self.filename = os.path.basename(self.path)


        super(FileM, self).__init__(self.text)
        self.type = Block.file
        self.range = Range(0,len(self.text))

        self.lineCount = 0

        self.file = self

        self.linePoses = self.__get_line_poses()
        self.errors = []


    def analyze(self):
        for child in self.children:
            child.analyze()






    def __get_line_poses(self):
        start = 0
        ret = []
        while True:
            pos = self.text.find("\n",start)
            if pos < 0:
                break
            ret.append(pos)
            start = pos+1
        return ret


    def ext(self):
        return self.ext


    def print_all_errors(self):
        print("===={}====".format(self.filename))
        errors = sorted(self.errors,key = lambda obj:obj.line)
        for e in errors:
            print(e)
