import folium
import pandas as pd
import numpy as np  # 基本工具包


# 中文转换函数，防止出现中文输入乱码的情况
def parse_zhch(s):
    return str(str(s).encode('ascii', 'xmlcharrefreplace'))[2:-1]


def BDS_plot(path):
    # 第一部分：文件读取
    # 显示规则
    pd.set_option('display.unicode.east_asian_width', True)
    # 读取文件信息
    # path = 'E:/python_project/BDS_map_and_speed/BDS_information.xlsx'
    df_loc = pd.read_excel(path,
                           sheet_name=0,
                           usecols=[0, 1],
                           header=1
                           )

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

    # 第四部分：地图可视化
    loc_map = folium.Map(
        location=loc[1],
        zoom_start=14,
        # tiles='Stamen Terrain'
        # tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',  # 高德街道图
        # tiles='https://mt.google.com/vt/lyrs=h&x={x}&y={y}&z={z}', # google 地图
        tiles='https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=7',  # 高德地图常规图
        # tiles='https://rt0.map.gtimg.com/tile?z={z}&x={x}&y={-y}',

        attr='default',
    )

    # 给地图添加定点标记，鼠标悬浮可显示自定义名称，可自定义图案、颜色，点击触发自定义名称固定显示
    folium.Marker(
        location=loc[0],
        popup=folium.Popup(html=parse_zhch('起始点')),
        tooltip=parse_zhch('起始点'),
        icon=folium.Icon(icon='cloud', color='red')
    ).add_to(loc_map)
    folium.Marker(
        location=loc[-1],
        popup=folium.Popup(html=parse_zhch('终点')),
        tooltip=parse_zhch('终点'),
        icon=folium.Icon(icon='info-sign', color='blue')
    ).add_to(loc_map)
    # 追加可以点击获得经纬度的功能
    loc_map.add_child(folium.LatLngPopup())
    # 追加地图轨迹
    folium.PolyLine(
        locations=[loc],
        popup=parse_zhch('路径'),
        color='green'
    ).add_to(loc_map)
    # 保存
    loc_map.save("./loc_map.html")
    pass
