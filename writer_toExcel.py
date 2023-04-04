#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : writer_toExcel.py
@Author: XuYaoJian
@Date  : 2023/2/15 19:40
@Desc  : 
"""
import pandas as pd
import openpyxl


def writer_toExcel_tiqian():
    with pd.ExcelWriter("./result/test2.xlsx", mode='a', engine='openpyxl') as writer:
        start = 103
        # biaoti = "Variable 1"
        for i in range(50):
            data = {}
            for j in range(start):
                data["Variable " + str(j + 1)] = []
            data = pd.DataFrame(data)
            data.to_excel(writer, sheet_name="data_" + str(start), index=False)
            start += 27

def writer_toExcel_zuihou():
    with pd.ExcelWriter("./result/test1.xlsx", mode='a', engine='openpyxl') as writer:
        start = 1453
        # biaoti = "Variable 1"
        for i in range(50):
            data = {}
            for j in range(start):
                data["Variable " + str(j + 1)] = []
            data = pd.DataFrame(data)
            data.to_excel(writer, sheet_name="data_" + str(start), index=False)
            start += 27

def writer_toExcel_qian50(final_sequences, start):
    with pd.ExcelWriter("./result/result.xlsx", mode='a', engine='openpyxl') as writer:
        data = {}
        for j in range(start):
            line = []
            for k in range(len(final_sequences)):
                line.append(final_sequences[k][j])
            data["Variable " + str(j + 1)] = line
        data = pd.DataFrame(data)
        data.to_excel(writer, sheet_name="data_" + str(start), index=False)


def writer_toExcel(final_sequences, start):
    with pd.ExcelWriter("./result/test2.xlsx", mode='a', engine='openpyxl') as writer:
        # start = 1453
        # for i in range(50):
        data = {}
        for j in range(start):
            line = []
            for k in range(len(final_sequences)):
                line.append(final_sequences[k][j])
            data["Variable " + str(j + 1)] = line
        data = pd.DataFrame(data)
        data.to_excel(writer, sheet_name="data_" + str(start), index=False)
            # start += 27

    # data = pd.DataFrame(
    #     {"col1": [1, 2, 3],
    #      "col2": [4, 5, 6],
    #      "col3": [7, 8, 9]
    #      }
    # )
    # with pd.ExcelWriter("./final_result/1.xlsx", mode='a', engine='openpyxl') as writer:
    #     data.to_excel(writer, sheet_name="这是追加的第1个sheet", index=False)
    #     data.to_excel(writer, sheet_name="这是追加的第2个sheet", index=False)

    # for i in range(100):

# if __name__ == '__main__':
    # writer_toExcel_zuihou()