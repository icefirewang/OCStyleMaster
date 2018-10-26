# -*- coding:utf-8 -*-

from .blockBase import *


class Comment_1(BlockBase):

    def __init__(self, text):
        super(Comment_1, self).__init__(text)
        self.type = Block.comment_1

    @classmethod
    def start_text(cls):
        return "//"

    @classmethod
    def end_text(cls):
        return "\n"



class Comment_N(BlockBase):


    def __init__(self,text):
        super(Comment_N, self).__init__(text)
        self.type = Block.comment_n


    @classmethod
    def start_text(cls):
        return "/\*"

    @classmethod
    def end_text(cls):
        return "\*/"