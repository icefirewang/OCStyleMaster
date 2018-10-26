# -*- coding:utf-8 -*-

from .blockBase import *
from config import *
from utils import *

class Property(BlockBase):

    def __init__(self, text):
        super(Property, self).__init__(text)
        self.type = Block.property


    @classmethod
    def config_rule_names(cls):
        return ["property"]

    def analyze(self):
        self.analyze_by_config()




    @classmethod
    def start_text(cls):
        return "@property"


    @classmethod
    def end_text(cls):
        return "\n"