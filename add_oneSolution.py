#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : add_oneSolution.py
@Author: XuYaoJian
@Date  : 2023/2/17 18:55
@Desc  : 
"""
# 添加一个A闪耀黑、探索绿插入到A闪耀黑，闪耀黑当中，减少喷头的清洗次数
import sys
from copy import deepcopy

from convert import convert_two_to_one


def check_solution(solution, seq_len=103):
    if len(solution) == seq_len:
        for i in range(seq_len):
            if i in solution:
                continue
            else:
                return 0
        return 1
    else:
        return 0


# 插入闪耀黑，探索绿1到n到前面
def add_oneSolution1(new_duan, information_new, results, start, shihei_flag):
    tansuolv_len = 0
    for i in range(len(new_duan[6]) - 1, -1, -1):
        if information_new[new_duan[6][i]][3] == 1 and information_new[new_duan[6][i]][1] == 8:
            tansuolv_len += 1
    if tansuolv_len < 1:
        return

    shanyaohei_er = []
    shanyaohei_si = []
    for i in range(len(new_duan[5])):
        if information_new[new_duan[5][i]][3] == 1:
            shanyaohei_si.append(new_duan[5][i])
        elif information_new[new_duan[5][i]][3] == 0:
            shanyaohei_er.append(new_duan[5][i])
        else:
            sys.exit("错erte误发生而且我平静安定")

    B_shanyaohei_len = len(new_duan[4]) - shihei_flag

    result_temp = []
    B_yu = B_shanyaohei_len % 5
    if B_yu == 4:
        result_temp.append(shanyaohei_er[0])
        shanyaohei_er.pop(0)
    elif B_yu == 3:
        result_temp.extend(shanyaohei_er[0:2])
        shanyaohei_er = shanyaohei_er[2:]
    elif B_yu == 2:
        result_temp.extend(shanyaohei_er[0:3])
        shanyaohei_er = shanyaohei_er[3:]
    elif B_yu == 1:
        result_temp.extend(shanyaohei_er[0:4])
        shanyaohei_er = shanyaohei_er[4:]

    for i in range(1, tansuolv_len + 1):
        result = deepcopy(result_temp)
        # 插入i个
        duan = deepcopy(new_duan)
        tansuolv = []
        flag_num = 0
        for j in range(len(duan[6]) - 1, -1, -1):
            if information_new[duan[6][j]][3] == 1 and information_new[duan[6][j]][1] == 8:
                tansuolv.append(duan[6][j])
                duan[6].pop(j)
                flag_num += 1
                if flag_num == i:
                    break
        # yuxia = len(shanyaohei_er) + len(shanyaohei_si) - (len(tansuolv) - 1) * 4
        # if yuxia % 5 != 0:
        duan[6].insert(0, tansuolv[-1])
        tansuolv.pop(len(tansuolv) - 1)
        pos1, pos2, pos3 = 0, 0, 0
        if len(tansuolv) > len(shanyaohei_er) * 3 or len(tansuolv) > len(shanyaohei_si):
            sys.exit("插入出现546了fawefafa")
        while pos1 < len(shanyaohei_er) and pos2 < len(shanyaohei_si) and pos3 < len(tansuolv):
            result.extend(shanyaohei_er[pos1:pos1 + 3])
            result.extend(shanyaohei_si[pos2:pos2 + 1])
            result.extend(tansuolv[pos3:pos3 + 1])
            pos1 += 3
            pos2 += 1
            pos3 += 1
        while pos1 < len(shanyaohei_er) and pos2 < len(shanyaohei_si):
            result.extend(shanyaohei_er[pos1:pos1 + 1])
            result.extend(shanyaohei_si[pos2:pos2 + 2])
            pos1 += 1
            pos2 += 2
        result.extend(shanyaohei_er[pos1:])
        # result.extend(shanyaohei_si[pos2:])
        duan[5] = result

        # 如果A闪耀黑，闪耀黑多了一个四驱车放在最后
        A_flag = 0
        for j in range(len(duan[5]) - 1, -1, -1):
            # 为四驱车，且不为探索绿
            if information_new[duan[5][j]][3] == 1 and information_new[duan[5][j]][1] != 8:
                is_siqu = information_new[duan[5][j - 1]][3]
                if is_siqu != 1:
                    duan[5][j], duan[5][-1] = duan[5][-1], duan[5][j]  # 四驱车和最后一个位置调换
                    A_flag = 1
                break
        if A_flag == 0:
            for j in range(len(duan[6]) - 1, -1, -1):
                if information_new[duan[6][j]][3] == 1:
                    if information_new[duan[6][j - 1]][3] != 1:
                        duan[6].insert(1, duan[6][j])  # 四驱车插入到第一个位置
                        duan[6].pop(j + 1)  # 删除四驱车
                    break

        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出错了！6而去214s")
        results.append(duan)


def add_oneSolution_commcon(one_duan1,one_duan2, information_new, start):
    duan1 = deepcopy(one_duan1)
    duan2 = deepcopy(one_duan2)
    tansuolv = []
    for i in range(len(duan2) - 1, -1, -1):
        if information_new[duan2[i]][3] == 1 and information_new[duan2[i]][1] == 8:
            tansuolv.append(duan2[i])
            duan2.pop(i)
    if len(tansuolv) < 3:
        print("没有了")
    if len(tansuolv) < 1:
        return duan1, duan2

    shanyaohei_er = []
    shanyaohei_si = []
    for i in range(len(duan1)):
        if information_new[duan1[i]][3] == 1:
            shanyaohei_si.append(duan1[i])
        elif information_new[duan1[i]][3] == 0:
            shanyaohei_er.append(duan1[i])
        else:
            sys.exit("错erte误发生而且我平静安定")

    result = []
    yuxia = len(shanyaohei_er) + len(shanyaohei_si) - (len(tansuolv) - 1) * 4
    if yuxia % 5 != 0:
        duan2.insert(0, tansuolv[-1])
        tansuolv.pop(len(tansuolv) - 1)
    pos1, pos2, pos3 = 0, 0, 0
    if start == 157:
        result.append(tansuolv[0])
        result.append(shanyaohei_er[0])
        result.extend(shanyaohei_si[:2])
        result.append(shanyaohei_er[1])
        result.append(tansuolv[1])
        result.append(shanyaohei_si[2])
        result.extend(shanyaohei_er[2:])
        duan1 = result
        # seq = convert_two_to_one(duan)
        # if check_solution(seq, start) != 1:
        #     sys.exit("序列出879674s")
        # results.append(duan)
        return duan1, duan2
    while pos1 < len(shanyaohei_er) and pos2 < len(shanyaohei_si) and pos3 < len(tansuolv):
        result.extend(shanyaohei_er[pos1:pos1 + 3])
        result.extend(shanyaohei_si[pos2:pos2 + 1])
        result.extend(tansuolv[pos3:pos3 + 1])
        pos1 += 3
        pos2 += 1
        pos3 += 1
    while pos1 < len(shanyaohei_er) and pos2 < len(shanyaohei_si):
        result.extend(shanyaohei_er[pos1:pos1 + 1])
        result.extend(shanyaohei_si[pos2:pos2 + 2])
        pos1 += 1
        pos2 += 2
    result.extend(shanyaohei_er[pos1:])
    # result.extend(shanyaohei_si[pos2:])
    duan1 = result

    # 如果A闪耀黑，闪耀黑多了一个四驱车放在最后
    for i in range(len(duan1) - 1, -1, -1):
        # 为四驱车，且不为探索绿
        if information_new[duan1[i]][3] == 1 and information_new[duan1[i]][1] != 8:
            is_siqu = information_new[duan1[i - 1]][3]
            if is_siqu != 1:
                duan1[i], duan1[-1] = duan1[-1], duan1[i]  # 四驱车和最后一个位置调换
            break

    # seq = convert_two_to_one(duan)
    # if check_solution(seq, start) != 1:
    #     sys.exit("序列出错了！--44674s")
    # results.append(duan)
    return duan1, duan2



def add_oneSolution(new_duan, information_new, results, start, shihei_flag):
    duan = deepcopy(new_duan)
    tansuolv = []
    for i in range(len(duan[6]) - 1, -1, -1):
        if information_new[duan[6][i]][3] == 1 and information_new[duan[6][i]][1] == 8:
            tansuolv.append(duan[6][i])
            duan[6].pop(i)
    if len(tansuolv) < 3:
        print("没有了")
    if len(tansuolv) < 1:
        return

    shanyaohei_er = []
    shanyaohei_si = []
    for i in range(len(duan[5])):
        if information_new[duan[5][i]][3] == 1:
            shanyaohei_si.append(duan[5][i])
        elif information_new[duan[5][i]][3] == 0:
            shanyaohei_er.append(duan[5][i])
        else:
            sys.exit("错erte误发生而且我平静安定")

    B_shanyaohei_len = len(duan[4]) - shihei_flag
    B_yu = B_shanyaohei_len % 5
    result = []
    if B_yu == 4:
        result.append(shanyaohei_er[0])
        shanyaohei_er.pop(0)
    elif B_yu == 3:
        result.extend(shanyaohei_er[0:2])
        shanyaohei_er = shanyaohei_er[2:]
    elif B_yu == 2:
        result.extend(shanyaohei_er[0:3])
        shanyaohei_er = shanyaohei_er[3:]
    elif B_yu == 1:
        if start == 157:
            result.extend(shanyaohei_si[:2])
            shanyaohei_si = shanyaohei_si[2:]
            result.extend(shanyaohei_er[:1])
            shanyaohei_er = shanyaohei_er[1:]
            result.extend(shanyaohei_si[:1])
            shanyaohei_si = shanyaohei_si[1:]
        else:
            result.extend(shanyaohei_er[0:4])
            shanyaohei_er = shanyaohei_er[4:]

    yuxia = len(shanyaohei_er) + len(shanyaohei_si) - (len(tansuolv) - 1) * 4
    if yuxia % 5 != 0:
        duan[6].insert(0, tansuolv[-1])
        tansuolv.pop(len(tansuolv) - 1)
    pos1, pos2, pos3 = 0, 0, 0
    if start == 157:
        result.append(tansuolv[0])
        result.append(shanyaohei_er[0])
        result.extend(shanyaohei_si[:2])
        result.append(shanyaohei_er[1])
        result.append(tansuolv[1])
        result.append(shanyaohei_si[2])
        result.extend(shanyaohei_er[2:])
        duan[5] = result
        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出879674s")
        results.append(duan)
        return duan

    while pos1 < len(shanyaohei_er) and pos2 < len(shanyaohei_si) and pos3 < len(tansuolv):
        result.extend(shanyaohei_er[pos1:pos1 + 3])
        result.extend(shanyaohei_si[pos2:pos2 + 1])
        result.extend(tansuolv[pos3:pos3 + 1])
        pos1 += 3
        pos2 += 1
        pos3 += 1
    while pos1 < len(shanyaohei_er) and pos2 < len(shanyaohei_si):
        result.extend(shanyaohei_er[pos1:pos1 + 1])
        result.extend(shanyaohei_si[pos2:pos2 + 2])
        pos1 += 1
        pos2 += 2
    result.extend(shanyaohei_er[pos1:])
    # result.extend(shanyaohei_si[pos2:])
    duan[5] = result

    # 如果A闪耀黑，闪耀黑多了一个四驱车放在最后
    for i in range(len(duan[5]) - 1, -1, -1):
        # 为四驱车，且不为探索绿
        if information_new[duan[5][i]][3] == 1 and information_new[duan[5][i]][1] != 8:
            is_siqu = information_new[duan[5][i - 1]][3]
            if is_siqu != 1:
                duan[5][i], duan[5][-1] = duan[5][-1], duan[5][i]  # 四驱车和最后一个位置调换
            break

    seq = convert_two_to_one(duan)
    if check_solution(seq, start) != 1:
        sys.exit("序列出错了！--44674s")
    results.append(duan)
    return duan
