# -*- coding:utf-8 -*-


g_global = None

class GlobalData:

    def __init__(self):
        self.configPath = None





def share():
    global g_global
    if g_global is None:
        g_global = GlobalData()
    return g_global