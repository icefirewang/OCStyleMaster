# -*- coding:utf-8 -*-


g_global = None
import os
import sys
import shutil

import importlib

class GlobalData:

    def __init__(self):
        self._root = None
        self._configPath = None
        self.targetPath = None
        self.outputPath = None
        self._config  = None



    def __remove_old_customer_config(self):
        pass

    def config(self):
        """
        获取配置
        :return:
        """
        if self._config is not None:
            return self._config

        if self._configPath is not None:
            self.__copy_customer_config()
            self._config = self.__get_customer_config()
        else:
            self._config = self.__get_default_config()

        return self._config

    def set_config_path(self,path):
        self._configPath = path


    def __get_customer_config(self):
        """
        获取自定义配置
        :return:
        """
        import OCStyleMaster.config.customerConfig as CustomerConfig
        return CustomerConfig.Config()

    def __get_default_config(self):
        """
        获取默认配置
        :return:
        """
        import OCStyleMaster.config.config as Config
        return Config.Config()

    def __copy_customer_config(self):
        targetPath = os.path.join(self.root(),"config","customerConfig.py")
        sourcePath = self._configPath
        return shutil.copyfile(sourcePath,targetPath)


    def config_path(self):
        if self._configPath is None:
            packagePath =  os.path.join(self._root,"config","config")
            self._configPath = packagePath
        return self._configPath


    def root(self):
        return self._root



def share():
    global g_global
    if g_global is None:
        g_global = GlobalData()
    return g_global