#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : readInfo.py
@Author: XuYaoJian
@Date  : 2023/2/8 10:44
@Desc  : 
"""
import csv


def read_info(filepath="./数据集/data_103.csv"):
    information = []
    original_information = []
    with open(filepath, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # 忽略第一行
        num = 0
        B_shanyaohei = 0
        B_yetaihui_siqu_num = 0
        for row in reader:
            car = []
            original_car = []
            if row[1] == 'A':
                car.append(0)
                original_car.append("A")
            elif row[1] == 'B':
                car.append(1)
                original_car.append("B")
            else:
                print("错误！！！！！！！！")
            if row[2] == '薄雾灰':
                car.append(0)
                original_car.append("薄雾灰")
            elif row[2] == '天空灰':
                car.append(1)
                original_car.append("天空灰")
            elif row[2] == '飞行蓝':
                car.append(2)
                original_car.append("飞行蓝")
            elif row[2] == '水晶紫':
                car.append(3)
                original_car.append("水晶紫")
            elif row[2] == '水晶珍珠白':
                car.append(4)
                original_car.append("水晶珍珠白")
            elif row[2] == '明亮红':
                car.append(5)
                original_car.append("明亮红")
            elif row[2] == '闪耀黑':
                car.append(6)
                original_car.append("闪耀黑")
            elif row[2] == '探索绿':
                car.append(8)
                original_car.append("探索绿")
            elif row[2] == '液态灰':
                car.append(9)
                original_car.append("液态灰")
            else:
                print("错误！！！！！！！！")
            if row[3] == '闪耀黑':
                car.append(6)
                original_car.append("闪耀黑") # 车顶
            elif row[3] == '石黑':
                car.append(7)
                original_car.append("石黑")  # 车顶
            elif row[3] == '探索绿':
                car.append(8)
                original_car.append("探索绿")  # 车顶
            elif row[3] == '无对比颜色':
                car.append(car[-1])
                original_car.append(original_car[-1])  # 车顶
            else:
                print("错误！！！！！！！！")
            if row[6] == '两驱':
                car.append(0)
                original_car.append("两驱")
            elif row[6] == '四驱':
                car.append(1)
                original_car.append("四驱")
            else:
                print("错误！！！！！！！！")

            if row[3] == '石黑' and row[2] == '闪耀黑':
                num += 1
            if row[3] == '无对比颜色' and row[2] == '闪耀黑' and row[1] == 'B':
                B_shanyaohei += 1
            if row[3] == '无对比颜色' and row[2] == '液态灰' and row[6] == '四驱':
                B_yetaihui_siqu_num += 1
            information.append(car)
            original_information.append(original_car)
        # print("石黑,闪耀黑有",num,"个")
        if num == 1:
            if B_shanyaohei < 12:
                print("石黑,闪耀黑有",num,"个")
                print("B闪耀黑,闪耀黑有", B_shanyaohei, "个")
        if num == 2:
            if B_shanyaohei < 25:
                print("石黑,闪耀黑有",num,"个")
                print("B闪耀黑,闪耀黑有", B_shanyaohei, "个")
        if B_yetaihui_siqu_num > 0:
            print("B液态灰,液态灰有", B_yetaihui_siqu_num, "个")

        return information, original_information