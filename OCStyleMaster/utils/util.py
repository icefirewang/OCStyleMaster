# -*- coding:utf-8 -*-

import os
class Util:

    @classmethod
    def extension(cls,path):
        l = os.path.splitext(path)
        ret =  l[1]
        return ret
