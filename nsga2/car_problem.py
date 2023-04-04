#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : car_problem.py
@Author: XuYaoJian
@Date  : 2022/12/9 22:11
@Desc  :
"""
import math

from nsga2.individual import Individual


# 问题建模
class Problem(object):
    def __init__(self, information, original_information=None):
        '''
        :param information:二维列表
        车型A,B：0，1
        变速器：二驱，四驱:0,1
        '''
        self.information = information
        self.original_information = original_information
        self.objectives = 4
        self.variables = len(information)

    def calculate_objectives(self, individual: Individual):
        solution = individual.features
        n = len(solution)

        type_change = 1

        current_type = self.information[solution[0]][0]

        sameCar_passed = 1  # // 先喷车顶，再喷车身。
        key_value = {5: 0, 4: 0, 3: 0, 2: 0}

        continue_four = 0
        continue_four_n = 0

        t1 = 0
        t2 = 0
        use_time = 0

        for i in range(0, len(solution)):
            type_ = self.information[solution[i]][0]
            if abs(type_ - current_type) > 0.1:  # 切换设备
                current_type = type_
                type_change += 1
                if use_time < 30 * 60:  # 如果这个类型的设备使用时间 < 30分钟，需要等待切换时间。
                    t1 += (30 * 60 - use_time + 80)  # 这辆车通过焊装车间的时间（焊装车间处理这辆车需要多长时间）。
                else:
                    t1 += 80
                use_time = 80  # 切换设备后，该设备使用时间。
            else:
                use_time += 80
                t1 += 80

            car_top = self.information[solution[i]][2]
            car_body = self.information[solution[i]][1]

            if i - 1 >= 0 and abs(car_top - self.information[solution[i - 1]][1]) > 0.1:
                t2 += 80

            if abs(car_top - car_body) > 0.1:
                t2 += 80

            t2 += 80

            same_color = self.information[solution[i]][2]

            if i > 0 and (self.information[solution[i]][1] == same_color) and (
                    self.information[solution[i - 1]][2] == same_color) and \
                    (self.information[solution[i - 1]][1] == same_color):
                sameCar_passed += 1
                if sameCar_passed == 5:
                    key_value[sameCar_passed] = key_value[sameCar_passed] + 1

                    if i + 1 < n and self.information[solution[i]][1] == self.information[solution[i + 1]][2]:
                        t2 += 80  # 强制清洗一次（本来不用清洗的）

                    if i + 1 < n and self.information[solution[i + 1]][2] == same_color and \
                            self.information[solution[i + 1]][1] == same_color:
                        sameCar_passed = 0
                    else:
                        sameCar_passed = 1

            else:
                if sameCar_passed > 1:
                    key_value[sameCar_passed] = key_value[sameCar_passed] + 1
                sameCar_passed = 1

            # 目标三
            if self.information[solution[i]][3] == 1:
                continue_four += 1
            else:
                if continue_four == 2 or continue_four == 3:  # 连续2、3辆四驱
                    continue_four_n += 1
                continue_four = 0

        # 目标二
        if sameCar_passed > 1:
            key_value[sameCar_passed] = key_value[sameCar_passed] + 1

        score = 0.0
        for i in range(2, 6):
            value = key_value[i]
            if i == 2:
                score += value
            elif i == 3:
                score += value * 3
            elif i == 4:
                score += value * 6
            else:
                score += value * 10

        if score == 0.0:
            score = 0.00001

        if continue_four == 2 or continue_four == 3:  # 连续2、3辆四驱
            continue_four_n += 1

        if continue_four_n == 0:
            continue_four_n = 0.00001

        # f1 = type_change / n * (1.0 / 1.1)
        # f2 = 10.0 / score * (1.0 / 1.1)
        # f3 = 1.0 / continue_four_n * (1.0 / 1.1)
        # f4 = (t1 + t2 + 80*n) / (50*24*3600) *(1.0/1.1)

        f1 = type_change / n
        f2 = 10.0 / score
        f3 = 1.0 / continue_four_n
        # print("continue_four:", continue_four_n)
        sum_t = t1 + t2 + 80 * n
        f4 = (t1 + t2 + 80 * n) / (50 * 24 * 3600)
        # print("t1:",t1,"t2:",t2)
        individual.objectives = [f1, f2, f3, f4]

# # 焊装车间设备切换次数
#    def objective1(self, individual: Individual):
#        num = 1
#        solution = individual.features
#        n = len(solution)
#        for i in range(1, n):
#            if self.information[solution[i]][0] != self.information[solution[i - 1]][0]:
#                num += 1
#        f1 = (num / n) * (1.0 / 1.1)
#        return f1


# car_top = self.information[solution[0]][2]
#        # 涂装车顶
#        t2 += 40
#        num = 0
#        if car_top != '无对比颜色':
#            # 清洗喷头
#            t2 += 80
#        else:
#            num = 1
#        # 涂装车身
#        t2 += 40
#        for i in range(1, len(solution)):
#            if num == 5:
#                # 清洗喷头
#                t2 += 80
#                num = 0
#            before_car_body = self.information[solution[i - 1]][1]
#
#            car_top = self.information[solution[i]][2]
#            car_body = self.information[solution[i]][1]
#
#            if (car_top == '无对比颜色' and car_body != before_car_body) or car_top != before_car_body:
#                if num != 0:
#                    # 清洗喷头
#                    t2 += 80
#                    num = 0
#            # 涂装车顶
#            t2 += 40
#
#            if car_top != '无对比颜色':
#                # 清洗喷头
#                t2 += 80
#                num = 0
#            # 涂装车身
#            t2 += 40
#            num += 1

# # 总装车间,四驱车连放次数<4，连放2次和3次同样好。
# # 出现一次两次连放加1分，出现一次三次连放加1分
# def objective3(self, individual: Individual):
#     solution = individual.features
#     n = len(solution)
#     score = 0.0
#     i = 0
#     while i < n:
#         if self.information[solution[i]][3] == 1:
#             num = 1
#             while (i + 1) < len(solution):
#                 i += 1
#                 if self.information[solution[i]][3] == 1:
#                     num += 1
#                 else:
#                     break
#             if 4 > num > 1:
#                 # score += 2.5
#                 score += 1.0
#         i += 1
#     # f3 = 0.1 / (score / n)
#     f3 = 1.0 / score * (1.0 / 1.1)
#     return f3


# # 当车进入涂装车间时,尽量连续生产颜色相同的车，且数量为5的倍数。(连续意思是至少两辆车连续)
# def objective2(self, individual: Individual):
#     # 生产连续5辆颜色相同的车得：10分,生产连续4辆颜色相同的车得：6分
#     # 生产连续3辆颜色相同的车得：3分,生产连续2辆颜色相同的车得：1分
#     # 生产连续1辆颜色相同的车得：0分,生产连续1辆颜色不相同的车得：0分
#     # notice:从开始进入或者切换喷头重新记录
#     solution = individual.features
#     n = len(solution)
#     num = 0
#     car_top = self.information[solution[0]][2]
#     a, b, c, d, e = 0, 0, 0, 0, 0
#     if car_top == '无对比颜色':
#         num = 1
#     for i in range(1, len(solution)):
#         before_car_top = self.information[solution[i - 1]][2]
#         before_car_body = self.information[solution[i - 1]][1]
#
#         car_top = self.information[solution[i]][2]
#         car_body = self.information[solution[i]][1]
#
#         if car_top == '无对比颜色' and before_car_top == '无对比颜色' and car_body == before_car_body:
#             num += 1
#             if num == 5:
#                 a += 1
#                 num = 0
#         elif car_top == '无对比颜色':
#             if num == 4:
#                 b += 1
#             elif num == 3:
#                 c += 1
#             elif num == 2:
#                 d += 1
#             num = 1
#         else:
#             if num == 4:
#                 b += 1
#             elif num == 3:
#                 c += 1
#             elif num == 2:
#                 d += 1
#             elif num == 1:
#                 e += 1
#             num = 0
#     if num == 4:
#         b += 1
#     elif num == 3:
#         c += 1
#     elif num == 2:
#         d += 1
#     elif num == 1:
#         e += 1
#     score = a * 10.0 + b * 6.0 + c * 3.0 + d * 1.0 + e * 0
#     f2 = 10 / score * (1.0 / 1.1)
#     # f2 = 0.05 / (score / n)
#     return f2
