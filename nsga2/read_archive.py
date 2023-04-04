#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : read_archive.py
@Author: XuYaoJian
@Date  : 2023/2/7 20:37
@Desc  : 
"""
import csv

import numpy as np
import pandas as pd

from nsga2.individual import Individual
from nsga2.car_problem import Problem
from nsga2.population import Population

from nsga2.print_solution import print_solution

def readSolutions(filepath, problem: Problem):
    sequences = pd.read_csv(filepath, header=None, sep=" ")
    sequences = sequences.dropna(axis=1, how="all")  # 删除表中全部为NaN的列
    sequences = np.array(sequences.values)
    sequences = list(sequences)
    population = Population()
    for i in range(len(sequences)):
        individual = Individual()
        individual.features = sequences[i]
        problem.calculate_objectives(individual)
        # print_solution(individual, problem)
        population.append(individual)

    # objv = [i.objectives for i in population]
    # hv_value = hv(objv, np.array([1.0, 1.0, 1.0, 1.0]))
    # print(hv_value)

    return population

# def read_info(filepath="../数据集/data_103.csv"):
#     information = []
#     with open(filepath, 'r', encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile)
#         header = next(reader)  # 忽略第一行
#         for row in reader:
#             car = []
#             if row[1] == 'A':
#                 car.append(0)
#             elif row[1] == 'B':
#                 car.append(1)
#             else:
#                 print("错误！！！！！！！！")
#             if row[2] == '薄雾灰':
#                 car.append(0)
#             elif row[2] == '天空灰':
#                 car.append(1)
#             elif row[2] == '飞行蓝':
#                 car.append(2)
#             elif row[2] == '水晶紫':
#                 car.append(3)
#             elif row[2] == '水晶珍珠白':
#                 car.append(4)
#             elif row[2] == '明亮红':
#                 car.append(5)
#             elif row[2] == '闪耀黑':
#                 car.append(6)
#             elif row[2] == '探索绿':
#                 car.append(8)
#             elif row[2] == '液态灰':
#                 car.append(9)
#             else:
#                 print("错误！！！！！！！！")
#             if row[3] == '闪耀黑':
#                 car.append(6)
#             elif row[3] == '石黑':
#                 car.append(7)
#             elif row[3] == '探索绿':
#                 car.append(8)
#             elif row[3] == '无对比颜色':
#                 car.append(car[-1])
#             else:
#                 print("错误！！！！！！！！")
#             if row[6] == '两驱':
#                 car.append(0)
#             elif row[6] == '四驱':
#                 car.append(1)
#             else:
#                 print("错误！！！！！！！！")
#             information.append(car)
#         return information


# if __name__ == '__main__':
#     start = 103
#     sum_hv = 0
#     for i in range(100):
#         filename = "data_" + str(start) + ".csv"
#         information = read_info("../数据集/"+filename)
#         problem = Problem(information=information)
#         _,  hv_value = readSolutions("../archive/data_" + str(start) + "_archive_VAR.txt", problem)
#         sum_hv += hv_value
#         start += 27
#     print("sum_hv = ")
#     print(sum_hv)
