#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : test1.py
@Author: XuYaoJian
@Date  : 2023/2/8 16:09
@Desc  :
"""
import sys
from copy import copy, deepcopy

import numpy as np

from nsga2.readInfo import read_info
from nsga2.metrics import hv
from nsga2.print_solution import print_solution
from nsga2.individual import Individual
from nsga2.car_problem import Problem
import pandas as pd
from convert import convert, convert_two_to_one
from nsga2.population import Population
# from nsga2.code.utils import *
from nsga2.utils import *
from add_oneSolution import add_oneSolution, add_oneSolution1, add_oneSolution_commcon
from nsga2.read_archive import readSolutions

from writer_toExcel import *

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

# main1和main2的区别只有一行代码，在第116行加了 if information_new[seq[pos1]][3] == 1: break
# 如果两个文件合并跑，hv整体会减少0.0002
# 而且main2不需要读取存档，main2跑出来的解支配了存档中的解
def data_373_b(start):
    # start = 373
    sum_hv = 0
    for g in range(1):
        print(start)
        information_new, original_information = read_info("./数据集/data_" + str(start) + ".csv")
        problem = Problem(information=information_new, original_information=original_information)
        pop_new = Population()

        if g > -1:
            results = []
            new_duan = []
            information = copy(information_new)
            unames = ['车型', '车身颜色', '车顶颜色', '变速器']
            information = pd.DataFrame(information, columns=unames)
            information = information.sort_values(by=['车型', '车身颜色', '车顶颜色', '变速器'])

            information['flag'] = information['车型'].astype(str) + information['车身颜色'].astype(str) + information[
                '车顶颜色'].astype(str)

            sequence = np.array(information.index)

            flag = list(information['flag'])

            flags = information['flag'].unique()
            final = []
            count = 0

            erqu = []
            siqu = []

            type_flag = 0

            for flag in flags:
                ttt = np.array(information[information['flag'] == flag].index)
                count += len(ttt)
                # print("正确长度:")
                # print(count)
                biansuqi = np.array(information[information['flag'] == flag]['变速器'])

                if type_flag == 0 and information_new[ttt[0]][0] == 1:
                    type_flag = 1
                    pos1, pos2 = 0, 0
                    c = []
                    while pos1 < len(erqu) and pos2 < len(siqu):
                        c.extend(erqu[pos1:pos1 + 1])
                        c.extend(siqu[pos2:pos2 + 2])
                        pos1 += 1
                        pos2 += 2
                    c.extend(erqu[pos1:])
                    c.extend(siqu[pos2:])
                    final.extend(c)
                    new_duan.append(c)  # 分段
                    erqu = []
                    siqu = []

                charudian = -1
                if (information_new[ttt[0]][2] != information_new[ttt[0]][1]) \
                        and len(final) != 0 and information_new[final[-1]][2] == information_new[final[-1]][1] \
                        and information_new[ttt[0]][1] == information_new[final[-1]][
                    1]:  # 当前车顶车身颜色不相同且前面车辆颜色相同，且当前车身颜色和前面车颜色相同
                    samecolor = information_new[final[-1]][1]

                    for i in range(len(final) - 2, -1, -1):
                        if (information_new[final[i]][2] != samecolor) and (
                                information_new[final[i]][1] != samecolor):  # 为0没有考虑
                            charudian = i + 1
                            break

                    if charudian == -1:
                        charudian = 0

                seq = list(ttt)
                biansuqi_seq = list(biansuqi)
                if charudian != -1:
                    pos1 = 0
                    duan_flag = 0
                    while charudian < len(final) and pos1 < len(seq):
                        # 全部插入
                        final.insert(charudian, seq[pos1])
                        new_duan[-1].insert(duan_flag, seq[pos1])

                        seq.pop(pos1)
                        biansuqi_seq.pop(pos1)
                        charudian += 6
                        duan_flag += 6

                ans = 0
                for i in range(len(biansuqi_seq)):
                    if biansuqi_seq[i] == 1:
                        ans = 1
                        a = seq[:i]
                        b = seq[i:]

                        if information_new[seq[0]][2] != information_new[seq[0]][1]:
                            erqu.extend(a)
                            siqu.extend(b)
                            break
                        else:
                            pos1, pos2 = 0, 0
                            c = []
                            while pos1 < len(a) and pos2 < len(b):
                                c.extend(a[pos1:pos1 + 1])
                                c.extend(b[pos2:pos2 + 2])
                                pos1 += 1
                                pos2 += 2
                            c.extend(a[pos1:])
                            c.extend(b[pos2:])
                            final.extend(c)
                            new_duan.append(c)  # 分段
                            break

                if ans == 0 and len(seq) != 0:
                    if information_new[seq[0]][2] == information_new[seq[0]][1]:
                        final.extend(seq)
                        new_duan.append(seq)  # 分段
                    else:
                        erqu.extend(seq)

                # print("final长度:")
                # print(len(final))

            pos1, pos2 = 0, 0
            c = []
            while pos1 < len(erqu) and pos2 < len(siqu):
                c.extend(erqu[pos1:pos1 + 1])
                c.extend(siqu[pos2:pos2 + 2])
                pos1 += 1
                pos2 += 2
            c.extend(erqu[pos1:])
            c.extend(siqu[pos2:])
            final.extend(c)
            new_duan.append(c)  # 分段

            # print("final长度:")
            # print(len(final))

            is_vaild = check_solution(final, start)
            if is_vaild != 1:
                print("不合法")

            # if len(new_duan) != 9:
            #     fix_duan(new_duan, information_new, start)

            # if len(new_duan) == 9:
                #  调整到固定顺序
                # B在前，A在后
            a1, a2, a3, a4, a5, a6, a7, a8, a9 = [], [], [], [], [], [], [], [], []
            for one in new_duan:
                if information_new[one[-1]][0] == 1 and information_new[one[-1]][1] == 1 and \
                        information_new[one[-1]][2] == 1:
                    a1 = one
                elif information_new[one[-1]][0] == 1 and information_new[one[-1]][1] == 4 and \
                        information_new[one[-1]][2] == 4:
                    a2 = one
                elif information_new[one[-1]][0] == 1 and information_new[one[-1]][1] == 9 and \
                        information_new[one[-1]][2] == 9:
                    a3 = one
                elif information_new[one[-1]][0] == 1 and information_new[one[-1]][1] != information_new[one[-1]][
                    2]:
                    a4 = one
                elif information_new[one[-1]][0] == 1 and information_new[one[-1]][1] == 6 and \
                        information_new[one[-1]][2] == 6:
                    a5 = one
                elif information_new[one[-1]][0] == 0 and information_new[one[-1]][1] == 6 and \
                        information_new[one[-1]][2] == 6:
                    a6 = one
                elif information_new[one[-1]][0] == 0 and information_new[one[-1]][1] != information_new[one[-1]][
                    2]:
                    a7 = one
                elif information_new[one[-1]][0] == 0 and information_new[one[-1]][1] == 4 and \
                        information_new[one[-1]][2] == 4:
                    a8 = one
                elif information_new[one[-1]][0] == 0 and information_new[one[-1]][1] == 1 and \
                        information_new[one[-1]][2] == 1:
                    a9 = one
                else:
                    sys.exit("duan错误")
            new_duan = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
            # else:
            #     sys.exit("new_duan不到9")

            B_siqu_len = 0
            B_erqu_array = []
            B_siqu_array = []
            B_shihei_array = []
            for number in new_duan[4]:
                if information_new[number][2] == 7 and information_new[number][1] == 6:  # 车顶：石黑 车身：闪耀黑
                    B_shihei_array.append(number)
                elif information_new[number][3] == 1:
                    B_siqu_array.append(number)
                    B_siqu_len += 1
                elif information_new[number][3] == 0:
                    B_erqu_array.append(number)
                else:
                    sys.exit("错eq误wqaqweasqq")
            shihei_flag = 0
            if len(B_shihei_array) == 2:
                new_duan[4][1], new_duan[4][3] = new_duan[4][3], new_duan[4][1]
                new_duan[4][4], new_duan[4][7] = new_duan[4][7], new_duan[4][4]
                shihei_flag = 2
            elif len(B_shihei_array) == 1:
                shihei_flag = 1
            elif len(B_shihei_array) > 2:
                sys.exit("错das误agqwqwqq")

            B_luan_siqu_len = 0
            for number in new_duan[3]:
                if information_new[number][3] == 1:
                    B_luan_siqu_len += 1

            if B_luan_siqu_len % 2 == 1:
                for i in range(len(new_duan[3]) - 1, -1, -1):
                    if information_new[new_duan[3][i]][3] == 1:
                        new_duan[3][i], new_duan[3][-1] = new_duan[3][-1], new_duan[3][i]  # 四驱车插入到最后
                        break

            if B_siqu_len % 2 == 1 and B_luan_siqu_len % 2 == 1:
                B_shihei_shanyao_len = len(B_shihei_array)
                if B_shihei_shanyao_len == 0:
                    for i in range(len(new_duan[4]) - 1, -1, -1):
                        if information_new[new_duan[4][i]][3] == 1:
                            new_duan[4].insert(0, new_duan[4][i])  # 四驱车插入到第一个位置
                            new_duan[4].pop(i + 1)  # 删除四驱车
                            break
                if B_shihei_shanyao_len == 1:
                    a = new_duan[4][0]
                    new_duan[4].pop(0)
                    for i in range(len(new_duan[4]) - 1, -1, -1):
                        if information_new[new_duan[4][i]][3] == 1:
                            new_duan[4].insert(0, new_duan[4][i])  # 四驱车插入到第一个位置
                            new_duan[4].pop(i + 1)  # 删除四驱车
                            new_duan[4].insert(5, a)
                            break
                if B_shihei_shanyao_len == 2:
                    a = new_duan[4][0]
                    new_duan[4].pop(0)
                    b = new_duan[4][5]
                    new_duan[4].pop(5)
                    new_duan[4].insert(0, new_duan[4][-1])  # 差一个二驱到最前面
                    new_duan[4].pop(len(new_duan[4]) - 1)
                    for i in range(len(new_duan[4]) - 1, -1, -1):
                        if information_new[new_duan[4][i]][3] == 1:
                            new_duan[4].insert(0, new_duan[4][i])  # 四驱车插入到第一个位置
                            new_duan[4].pop(i + 1)  # 删除四驱车
                            new_duan[4].insert(5, a)
                            new_duan[4].insert(16, b)
                            break

            add_oneSolution(new_duan, information_new, results, start, shihei_flag)  # 后期关键代码
            # add_oneSolution1(new_duan, information_new, results, start, shihei_flag)  # 后期关键代码

            # 1、类型A和类型B用天空灰连接
            duan = deepcopy(new_duan)
            flag, duan = connect_tiankonghui_BA(duan, information_new)
            if flag == 1:
                # 交换位置
                duan.insert(5, deepcopy(duan[0]))
                duan.pop(0)
                duan.insert(5, deepcopy(duan[8]))
                duan.pop(len(duan) - 1)
                seq = convert_two_to_one(duan)
                if check_solution(seq, start) != 1:
                    sys.exit("序列出312错了q！of4ak921")
                results.append(duan)  # 增加一个解

                a, b = add_oneSolution_commcon(duan[6], duan[7], information_new, start)  # 后期关键代码
                duan[6] = a
                duan[7] = b
                seq = convert_two_to_one(duan)
                if check_solution(seq, start) != 1:
                    sys.exit("序列出错23了9921")
                results.append(duan)  # 增加一个解

            # 2、类型A和类型B用水晶珍珠白连接
            duan = deepcopy(new_duan)
            flag, duan = connect_shuijing_BA(duan, information_new)
            if flag == 1:
                # 交换位置
                duan.insert(5, deepcopy(duan[1]))
                duan.pop(1)
                duan.insert(5, deepcopy(duan[7]))
                duan.pop(len(duan) - 2)

                seq = convert_two_to_one(duan)
                if check_solution(seq, start) != 1:
                    sys.exit("序列出fasd9211")
                results.append(duan)  # 增加一个解

                a, b = add_oneSolution_commcon(duan[6], duan[7], information_new, start)  # 后期关键代码
                duan[6] = a
                duan[7] = b
                seq = convert_two_to_one(duan)
                if check_solution(seq, start) != 1:
                    sys.exit("序列出321错][p;;1")
                results.append(duan)  # 增加一个解



            tansuo_flag = 0
            for i in range(len(new_duan[6]) - 1, -1, -1):
                if information_new[new_duan[6][i]][1] == 8:
                    a = new_duan[6][i]
                    b = new_duan[6][i - 1]
                    c = new_duan[6][i - 2]
                    if information_new[b][3] == 1:
                        new_duan[6] = new_duan[6][:i - 2] + new_duan[6][i + 1:]
                        new_duan[6].insert(0, c)
                        new_duan[6].insert(0, b)
                        new_duan[6].insert(0, a)
                        tansuo_flag = 2  # 不同颜色四驱车为偶数
                    else:
                        new_duan[6].pop(i)
                        new_duan[6].insert(0, a)
                        tansuo_flag = 1  # 不同颜色四驱车为单数
                    break
                # elif information_new[new_duan[6][i]][3] == 1:
                #     a = new_duan[6][i]
                #     b = new_duan[6][i - 1]
                #     c = new_duan[6][i - 2]
                #     if information_new[b][3] != 1:
                #         new_duan[6].pop(i)
                #         new_duan[6].insert(0, a)
                #         tansuo_flag = 1  # 不同颜色四驱车为单数
                #     break

            A_siqu_len = 0
            for number in new_duan[5]:
                if information_new[number][3] == 1:
                    A_siqu_len += 1
            if A_siqu_len % 2 == 1 and tansuo_flag == 1:
                for i in range(len(new_duan[5]) - 1, -1, -1):
                    if information_new[new_duan[5][i]][3] == 1:
                        new_duan[5][i], new_duan[5][-1] = new_duan[5][-1], new_duan[5][i]  # 四驱车和最后一个位置调换
                        break


            seq = convert_two_to_one(new_duan)
            if check_solution(seq, start) != 1:
                sys.exit("序列出错了！lfads")
            results.append(new_duan)  # 第一个解

            if B_luan_siqu_len % 2 == 1 and B_siqu_len % 2 == 0 and A_siqu_len % 2 == 0 and tansuo_flag == 1:
                print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1")  # 3

            if B_luan_siqu_len % 2 == 1 and B_siqu_len % 2 == 0 and A_siqu_len % 2 == 1 and (
                    tansuo_flag == 0 or tansuo_flag == 2):
                print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa2")  # 1

            if B_luan_siqu_len % 2 == 0 and B_siqu_len % 2 == 1 and A_siqu_len % 2 == 0 and tansuo_flag == 1:
                print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa3")  # 3

            # if B_luan_siqu_len % 2 == 1 and B_siqu_len % 2 == 1 and A_siqu_len % 2 == 1 and tansuo_flag == 1:
            #     print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa4") #6

            # sequences = convert(results)

            # is_vaild = check_solution(sequences[0], start)
            # if is_vaild != 1:
            #     sys.exit("不合法ewqeqwe")

            # 1、类型A和类型B用天空灰连接
            duan = deepcopy(new_duan)
            flag, duan = connect_tiankonghui_AB(duan, information_new)
            if flag == 1:
                # 交换位置
                duan.append(deepcopy(duan[0]))
                duan.pop(0)
                seq = convert_two_to_one(duan)
                if check_solution(seq, start) != 1:
                    sys.exit("序列出错iuyi9800921")
                results.append(duan)  # 增加一个解

            # 2、类型A和类型B用水晶珍珠白连接
            duan = deepcopy(new_duan)
            flag, duan = connect_shuijing_AB(duan, information_new)
            if flag == 1:
                # 交换位置
                duan.append(deepcopy(duan[1]))
                duan.pop(1)
                duan[6], duan[7] = duan[7], duan[6]
                seq = convert_two_to_one(duan)
                if check_solution(seq, start) != 1:
                    sys.exit("序列出错48/331224=9211")
                results.append(duan)  # 增加一个解

            # 3、类型A和类型B用闪耀黑连接
            duan = deepcopy(new_duan)
            # 情况一：A不同颜色车和A闪耀黑各自多了一个四驱车
            # if A_siqu_len % 2 == 1 and tansuo_flag == 1:
            #     pass  # 包含在前面的情况了
            # 情况二：A闪耀黑和B闪耀黑各自多了一个四驱车
            temp_duan = deepcopy(new_duan)
            if A_siqu_len % 2 == 1 and B_siqu_len % 2 == 1 and tansuo_flag != 1 and B_luan_siqu_len % 2 == 0:
                for i in range(len(temp_duan[5]) - 1, -1, -1):
                    if information_new[temp_duan[5][i]][3] == 1:
                        temp_duan[5].insert(0, temp_duan[5][i])  # 四驱车插入到第一个位置
                        temp_duan[5].pop(i + 1)  # 删除四驱车
                        break
                for i in range(len(temp_duan[4]) - 1, -1, -1):
                    if information_new[temp_duan[4][i]][3] == 1:
                        temp_duan[4][i], temp_duan[4][-1] = temp_duan[4][-1], temp_duan[4][i]  # 四驱车插入到最后
                        break
                seq = convert_two_to_one(temp_duan)
                if check_solution(seq, start) != 1:
                    sys.exit("序列出错了！123eq二32")
                results.append(temp_duan)  # 增加一个解
            # 情况三：A不同颜色车和B闪耀黑各自多了一个四驱车(这样可能会破坏连续生产五辆相同颜色的闪耀黑)
            temp_duan = deepcopy(new_duan)
            if B_siqu_len % 2 == 1 and tansuo_flag == 1 and A_siqu_len % 2 == 0 and B_luan_siqu_len % 2 == 0:
                for i in range(len(temp_duan[4]) - 1, -1, -1):
                    if information_new[temp_duan[4][i]][3] == 1:
                        temp_duan[4][i], temp_duan[4][-1] = temp_duan[4][-1], temp_duan[4][i]  # 四驱车插入到最后
                        break
                temp_duan[5], temp_duan[6] = temp_duan[6], temp_duan[5]  # 交换位置
                seq = convert_two_to_one(temp_duan)
                if check_solution(seq, start) != 1:
                    sys.exit("序列出错了！3124")
                results.append(temp_duan)  # 增加一个解

            # 情况四：B不同颜色车和B闪耀黑各自多了一个四驱车, 这个应该放到最前面
            # if B_siqu_len % 2 == 1 and B_luan_siqu_len % 2 == 1:
            #     pass  # 包含在前面的情况了

            # 情况五：B不同颜色车和A不同颜色车各自多了一个四驱车(这样可能会减少连续生产五辆颜色相同的闪耀黑)
            temp_duan = deepcopy(new_duan)
            if tansuo_flag == 1 and B_luan_siqu_len % 2 == 1 and A_siqu_len % 2 == 0 and B_siqu_len % 2 == 0:
                #  交换位置
                temp_duan[3], temp_duan[4] = temp_duan[4], temp_duan[3]
                temp_duan[5], temp_duan[6] = temp_duan[6], temp_duan[5]
                seq = convert_two_to_one(temp_duan)
                if check_solution(seq, start) != 1:
                    sys.exit("序列出错了！asfdasop3124")
                results.append(temp_duan)  # 增加一个解

            # 情况六：B不同颜色车和A闪耀黑各自多了一个四驱车(这样可能会减少连续生产五辆颜色相同的闪耀黑)
            temp_duan = deepcopy(new_duan)
            if B_luan_siqu_len % 2 == 1 and A_siqu_len % 2 == 1 and B_siqu_len % 2 == 0 and tansuo_flag != 1:
                temp_duan[3], temp_duan[4] = temp_duan[4], temp_duan[3]  # 交换位置
                for i in range(len(temp_duan[5]) - 1, -1, -1):
                    if information_new[temp_duan[5][i]][3] == 1:
                        temp_duan[5].insert(0, temp_duan[5][i])  # 四驱车插入到第一个位置
                        temp_duan[5].pop(i + 1)  # 删除四驱车
                        break
                seq = convert_two_to_one(temp_duan)
                if check_solution(seq, start) != 1:
                    sys.exit("序列出错了！3uiu")
                results.append(temp_duan)  # 增加一个解

            # 4、类型A和类型B交叉连接（用来增加连续生产五辆颜色相同的车，但同时会增加设备切换次数和设备的等待时间）
            # 情况一：连接方式1：B水晶B液态灰B乱B闪耀黑A闪耀黑A乱A水晶A天空灰B天空灰(在3闪耀黑连接中，再增加这样的连接方法。直接复制过来，虽然很多代码重复了，懒得管了)
            # 情况二：连接方式2：B天空灰B液态灰B乱B闪耀黑A闪耀黑A乱A天空灰A水晶B水晶(在3闪耀黑连接中，再增加这样的连接方法。直接复制过来，虽然很多代码重复了，懒得管了)
            # 情况三：连接方式3：B液态灰B乱B闪耀黑A闪耀黑A乱A水晶B水晶B天空灰A天空灰(在3闪耀黑连接中，再增加这样的连接方法。直接复制过来，虽然很多代码重复了，懒得管了)

            ans_flag = 0
            # A闪耀黑和B闪耀黑各自多了一个四驱车
            if A_siqu_len % 2 == 1 and B_siqu_len % 2 == 1 and tansuo_flag != 1 and B_luan_siqu_len % 2 == 0:
                ans_flag = 1
                temp_duan = deepcopy(new_duan)
                for i in range(len(temp_duan[5]) - 1, -1, -1):
                    if information_new[temp_duan[5][i]][3] == 1:
                        temp_duan[5].insert(0, temp_duan[5][i])  # 四驱车插入到第一个位置
                        temp_duan[5].pop(i + 1)  # 删除四驱车
                        break
                for i in range(len(temp_duan[4]) - 1, -1, -1):
                    if information_new[temp_duan[4][i]][3] == 1:
                        temp_duan[4][i], temp_duan[4][-1] = temp_duan[4][-1], temp_duan[4][i]  # 四驱车插入到最后
                        break
                connect(temp_duan, information_new, start, results)
            # A不同颜色车和B闪耀黑各自多了一个四驱车(这样可能会破坏连续生产五辆相同颜色的闪耀黑)
            elif B_siqu_len % 2 == 1 and tansuo_flag == 1 and A_siqu_len % 2 == 0 and B_luan_siqu_len % 2 == 0:
                ans_flag = 1
                temp_duan = deepcopy(new_duan)
                connect(temp_duan, information_new, start, results)

                temp_duan = deepcopy(new_duan)
                for i in range(len(temp_duan[4]) - 1, -1, -1):
                    if information_new[temp_duan[4][i]][3] == 1:
                        temp_duan[4][i], temp_duan[4][-1] = temp_duan[4][-1], temp_duan[4][i]  # 四驱车插入到最后
                        break
                temp_duan[5], temp_duan[6] = temp_duan[6], temp_duan[5]  # 交换位置
                connect(temp_duan, information_new, start, results)  # 这里有bug
            # B不同颜色车和A不同颜色车各自多了一个四驱车(这样可能会减少连续生产五辆颜色相同的闪耀黑)
            elif tansuo_flag == 1 and B_luan_siqu_len % 2 == 1 and A_siqu_len % 2 == 0 and B_siqu_len % 2 == 0:
                ans_flag = 1
                temp_duan = deepcopy(new_duan)
                connect(temp_duan, information_new, start, results)

                temp_duan = deepcopy(new_duan)
                #  交换位置
                temp_duan[3], temp_duan[4] = temp_duan[4], temp_duan[3]
                temp_duan[5], temp_duan[6] = temp_duan[6], temp_duan[5]
                connect_other(temp_duan, information_new, start, results)  # 这里有bug
            # B不同颜色车和A闪耀黑各自多了一个四驱车(这样可能会减少连续生产五辆颜色相同的闪耀黑)
            elif B_luan_siqu_len % 2 == 1 and A_siqu_len % 2 == 1 and B_siqu_len % 2 == 0 and tansuo_flag != 1:
                ans_flag = 1
                temp_duan = deepcopy(new_duan)
                connect(temp_duan, information_new, start, results)

                temp_duan = deepcopy(new_duan)
                temp_duan[3], temp_duan[4] = temp_duan[4], temp_duan[3]  # 交换位置
                for i in range(len(temp_duan[5]) - 1, -1, -1):
                    if information_new[temp_duan[5][i]][3] == 1:
                        temp_duan[5].insert(0, temp_duan[5][i])  # 四驱车插入到第一个位置
                        temp_duan[5].pop(i + 1)  # 删除四驱车
                        break
                connect2(temp_duan, information_new, start, results)
            else:
                connect(temp_duan, information_new, start, results)

            car_sequences = convert(results)
            for one_seq in car_sequences:
                is_hefa = check_solution(one_seq, start)
                if is_hefa != 1:
                    sys.exit("序列错误了！lsydfaasdlsdk312f")
                solution = Individual()
                solution.features = one_seq
                problem.calculate_objectives(solution)
                pop_new.append(solution)



        # solution = Individual()
        # solution.features = final
        # solution.features = sequences[0]

        # 读取存档中的解，之前用交叉变异搜索算法做时在小数据上面搜到了一些非支配解。
        # pop = readSolutions("../../archive/data_" + str(start) + "_archive_VAR.txt", problem=problem)
        # # #
        # for geti in pop:
        #     is_add = 1
        #     for new_geti in pop_new:
        #         if new_geti.dominates(geti):
        #             is_add = 0
        #             break
        #     if is_add == 1:
        #         pop_new.append(geti)
                # print(geti.objectives)


        # pop_new.extend(pop.population)
        # problem.calculate_objectives(individual=solution)
        # pop.append(solution)

        # objv = [i.objectives for i in pop]
        # objv = [i.objectives for i in pop_new]

        # final_sequences = [i.features for i in pop_new]

        # hv_value = hv([solution.objectives], np.array([1, 1, 1, 1]))

        # hv_value = hv(objv, np.array([1, 1, 1, 1]))
        # sum_hv += hv_value

        # writer_toExcel_qian50(final_sequences, start)

        # print_solution(pop_new.population[0], problem)

        # final = np.array([final]).astype(int)
        # np.savetxt("../result/" + str(start) + ".csv", final, delimiter=",", fmt='%d')

        start += 27

        # print(solution.objectives, hv_value)
        # print(objv, hv_value)
        # print(hv_value)
        return pop_new

    # print(sum_hv)
    # writer_toExcel_zuihou()
