#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : print_solution.py
@Author: XuYaoJian
@Date  : 2023/2/8 14:17
@Desc  : 
"""
from nsga2.car_problem import Problem


def print_solution(individual, problem: Problem):
    sequence = individual.features
    original_information = problem.original_information
    for i in range(len(sequence)):
        car_number = sequence[i]
        car_infomation = original_information[car_number]
        print(car_infomation[0] + "," + car_infomation[2] + "," + car_infomation[1] + "," + car_infomation[3])
