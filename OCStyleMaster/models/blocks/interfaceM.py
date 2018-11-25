# -*- coding:utf-8 -*-

from .property import *

class InterfaceM(BlockBase):

    def __init__(self, text):
        super(InterfaceM, self).__init__(text)
        self.type = Block.interface




    def analyze(self):
        self.__get_all_properties()
        for child in self.children:
            child.analyze()


    def __get_all_properties(self):
        regex = "@property .*;\s*\n"
        ranges = RegexUtil.full_search(regex,self.content())
        for r in ranges:
            property = Property(self.text)
            property.range.start = r[0] + self.range.start
            property.range.end = r[1] + self.range.start
            property.file = self.file
            property.parent = self.parent
            self.add_child(property)


    @classmethod
    def start_text(cls):
        return "@interface[^;]*\n"

    @classmethod
    def end_text(cls):
        return "@end"