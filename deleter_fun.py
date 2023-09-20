import glob
import os


def del_xlsx(path):
    # 使用glob获取文件夹中所有的.xlsx文件
    file_list = glob.glob(os.path.join(path, "*.xlsx"))
    # 删除所有.xlsx文件
    for file_path in file_list:
        os.remove(file_path)
        pass
    pass
