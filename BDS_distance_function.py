from geopy.distance import *
import pandas as pd
import numpy as np  # 基本工具包


def BDS_distance(path, width):
    # 第一部分：文件读取
    # 显示规则
    pd.set_option('display.unicode.east_asian_width', True)
    # 读取文件信息
    # path = 'E:/python_project/BDS_map_and_speed/BDS_information.xlsx'
    df_loc = pd.read_excel(path,sheet_name=0,usecols=[0, 1],header=1)

    # 第二部分:数据转换
    # 经度转换
    date_tr = df_loc.iloc[:, 0]
    date_array = np.array(date_tr)
    longitude = date_array.tolist()
    # # 纬度转换
    date_tr = df_loc.iloc[:, 1]
    date_array = np.array(date_tr)
    latitude = date_array.tolist()

    # 第三部分：数据组合
    j = len(latitude)
    k = len(longitude)
    if j != k:
        print('数据错误，请检查经纬度数据')
        pass
    else:
        loc = [[latitude[i], longitude[i]] for i in range(j)]
        pass

    # 第四部分：计算差值
    sum = 0
    for i in range(len(loc)):
        if i < len(loc) - 1:
            d = geodesic(loc[i], loc[i + 1]).m
            sum = sum + d
            pass
        else:
            pass
        pass
    # 第五部分：计算面积
    area = sum * width

    return [sum, area]
