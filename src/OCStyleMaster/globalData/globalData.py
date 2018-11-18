# -*- coding:utf-8 -*-


g_global = None
import os
import sys

class GlobalData:

    def __init__(self):
        self._root = None
        self._configPath = None
        self.targetPath = None
        self.outputPath = None


    def get_config(self):
        if self._configPath is not None:
            sys.path.insert(0,self._configPath)
        import config
        ret = config.config()
        return ret

    def set_config_path(self,path):
        self._configPath = path


    def config_path(self):
        if self._configPath is None:
            packagePath =  os.path.join(self._root,"config","config")
            self._configPath = packagePath
        return self._configPath





def share():
    global g_global
    if g_global is None:
        g_global = GlobalData()
    return g_global