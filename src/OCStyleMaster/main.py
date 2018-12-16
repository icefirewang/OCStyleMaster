
# -*- coding:utf-8 -*-

import argparse
import os
import traceback
from OCStyleMaster.globalData import *
from OCStyleMaster.tools import *
from OCStyleMaster.models import *
from OCStyleMaster.utils import *



def analyze_m_file(path):
    """
    分析 m 文件的入口函数
    :param path:
    :return:
    """
    file = FileM(path)
    blockAnalyzer = BlockAnalyzerM(file,0)
    blockAnalyzer.start()
    file.analyze()
    file.output_all_errors()


def analyze_h_file(path):
    """
    分析 .h 文件的入口函数
    :param path:
    :return:
    """
    file = FileH(path)
    blockAnalyzer = BlockAnalyzerH(file, 0)
    blockAnalyzer.start()
    file.analyze()
    file.output_all_errors()



def analyze_folder(path):
    """
    分析
    :param path:
    :return:
    """
    for dirpath,dirnames,filenames in os.walk(path):
        for name in filenames:
            path = dirpath + "/"+name
            try:
                analyze_path(path)
            except Exception as e:
                print("file error {}".format(path))
                print(e)
                traceback.print_exc()


def analyze_path(path):
    """
    分析文件/文件夹的统一入口
    :param path:
    :return:
    """
    extension = Util.extension(path)
    if extension == ".m":
        analyze_m_file(path)
    elif extension == ".h":
        analyze_h_file(path)
    elif extension == "":
        if os.path.isdir(path):
            analyze_folder(path)
    else:
        pass


def create_output_file():
    """
    创建输出文件
    :return: TRUE / FALSE
    """
    if GlobalData().outputPath is None:
        return True
    path = GlobalData().outputPath
    if os.path.isdir(path):
        print("输出文件路径为文件夹")
        return False
    if os.path.exists(path) == False:
        os.makedirs(path)
        return True

def check_config_exist(path):
    if os.path.exists(path) == False:
        return True
    sure = input("{} 已存在,是否覆盖？ y/n:".format(path))
    if sure.lower() == "y":
        return True
    elif sure.lower() == "n":
        return False
    else:
        return check_config_exist(path)


def export_config(path):
    """
    导出默认配置文件
    :param path:
    :return:
    """
    import shutil
    orgConfigPath = os.path.join(GlobalData().root(),"config","config.py")
    targetPath = None
    if os.path.isdir(path):
        targetPath = os.path.join(path,"config.py")
        if check_config_exist(targetPath) == False:
            return
    else:
        print("请输入正确文件夹路径")

    parentPath = os.path.split(path)[0]
    if os.path.exists(parentPath) == False:
        os.makedirs(parentPath)

    shutil.copyfile(orgConfigPath,targetPath)






def main():
    """
    主入口函数
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--file","-f",help="要分析的文件，或文件夹，文件必须是 .m 或 .h 文件（必选）")
    parser.add_argument("--exportConfiguration","-e",help="导出默认配置")
    parser.add_argument("--config","-c",help="配置路径")
    args = parser.parse_args()


    root = os.path.split(__file__)[0]
    GlobalData()._root = root

    configExportPath =  args.exportConfiguration
    filePath = args.file

    if filePath is None and configExportPath is None:
        print("-h 查看帮助")
        return

    if configExportPath is not None:
        export_config(configExportPath)
        return

    GlobalData().targetPath = filePath


    customerConfigPath = args.config
    if customerConfigPath is not None:
        if os.path.isfile(customerConfigPath) == False:
            print("您输入的配置文件不存在")
            return
        else:
            GlobalData()._configPath = args.config


    analyze_path(filePath)
    print("DONE !!!")





if __name__ == '__main__':
    main()