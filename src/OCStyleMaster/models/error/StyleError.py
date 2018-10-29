# -*- coding:utf-8 -*-

class StyleError:
    def __init__(self,line,pos,type,message):
        self.type = type
        self.line = line
        self.pos = pos
        self.message = message
        self.file = None


    def __str__(self):
        ret = "{} => [{}:{}] : {}".format(self.type,self.line,self.pos,self.message)
        return ret

