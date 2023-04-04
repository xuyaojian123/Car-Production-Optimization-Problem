#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : convert.py
@Author: XuYaoJian
@Date  : 2023/2/12 18:22
@Desc  : 
"""

from nsga2.readInfo import read_info


def convert(results):
    sequences = []
    for duan in results:
        seq = [i for j in duan for i in j]
        sequences.append(seq)
    return sequences


def convert_two_to_one(duan):
    seq = [i for j in duan for i in j]
    return seq

# start = 103
#
# for i in range(100):
#     print(i)
#     information_new, original_information = read_info("../../数据集/data_" + str(start) + ".csv")
#     start += 27
