
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



def main():
    """
    主入口函数
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--file","-f",help="要分析的文件，或文件夹，文件必须是 .m 或 .h 文件（必选）")
    parser.add_argument("--output", "-o", help="分析结果要导出的文件路径（可选）")
    parser.add_argument("--config","-c",help="配置路径")
    args = parser.parse_args()


    root = os.path.split(__file__)[0]
    GlobalData()._root = root

    filePath = args.file
    if filePath is None:
        print("请输入要分析的文件路径， -h 查看帮助")
        return

    GlobalData().targetPath = filePath
    GlobalData().outputPath = args.output
    GlobalData()._configPath = args.config

    if create_output_file():
        GlobalData()

    analyze_path(filePath)
    print("DONE !!!")





if __name__ == '__main__':
    main()