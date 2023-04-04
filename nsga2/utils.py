#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : utils.py
@Author: XuYaoJian
@Date  : 2023/2/13 15:24
@Desc  :
"""
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


def connect_tiankonghui_AB(duan, information_new):
    A_shihui_len = 0
    B_shihui_len = 0
    B_tiankonghui = []
    B_shihui_array = []
    for number in duan[0]:
        if information_new[number][2] == 7:
            B_shihui_len += 1
    for number in duan[8]:
        if information_new[number][2] == 7:
            A_shihui_len += 1
    A_changdu = len(duan[8]) - A_shihui_len
    B_changdu = len(duan[0]) - B_shihui_len
    for number in duan[0]:
        if information_new[number][2] == 7 and information_new[number][1] == 1:  # 车顶：石黑 车身：天空灰
            B_shihui_array.append(number)
        elif information_new[number][2] == 1 and information_new[number][1] == 1:  # 车顶：天空灰 车身：天空灰
            B_tiankonghui.append(number)
        else:
            sys.exit("错误e2qw121rt23")

    A_yu = A_changdu % 5
    B_yu = B_changdu % 5
    flag = 0
    if A_yu != 0 and B_yu != 0:
        flag = 1
        temp = []
        if A_yu == 4:
            duan[0].insert(0, duan[0][-1])
            duan[0].pop(len(duan[0]) - 1)
            temp = duan[0]
        elif A_yu == 3:
            temp.extend(B_tiankonghui[0:2])
            pos1, pos2 = 2, 0
            while pos1 < len(B_tiankonghui) and pos2 < len(B_shihui_array):
                temp.extend(B_shihui_array[pos2:pos2 + 1])
                temp.extend(B_tiankonghui[pos1:pos1 + 5])
                pos1 += 5
                pos2 += 1
            temp.extend(B_tiankonghui[pos1:])
            temp.extend(B_shihui_array[pos2:])
            # if pos1 < len(B_tiankonghui):
            #     sys.exit("长度出错了a[pk321fjl")
        elif A_yu == 2:
            temp.extend(B_tiankonghui[0:3])
            pos1, pos2 = 3, 0
            while pos1 < len(B_tiankonghui) and pos2 < len(B_shihui_array):
                temp.extend(B_shihui_array[pos2:pos2 + 1])
                temp.extend(B_tiankonghui[pos1:pos1 + 5])
                pos1 += 5
                pos2 += 1
            temp.extend(B_tiankonghui[pos1:])
            temp.extend(B_shihui_array[pos2:])
            # if pos1 < len(B_tiankonghui):
            #     sys.exit("长度出错了pio[778akfjl")
        elif A_yu == 1:
            temp.extend(B_tiankonghui[0:4])
            pos1, pos2 = 4, 0
            while pos1 < len(B_tiankonghui) and pos2 < len(B_shihui_array):
                temp.extend(B_shihui_array[pos2:pos2 + 1])
                temp.extend(B_tiankonghui[pos1:pos1 + 5])
                pos1 += 5
                pos2 += 1
            temp.extend(B_tiankonghui[pos1:])
            temp.extend(B_shihui_array[pos2:])
            # if pos1 < len(B_tiankonghui):
            #     sys.exit("长度出错了pi1237805l")
        else:
            sys.exit("错误WE57224AD")
        duan[0] = temp
    return flag, duan


def connect_tiankonghui_BA(duan, information_new):
    A_shihui_len = 0
    B_shihui_len = 0
    A_tiankonghui = []
    A_shihui_array = []
    for number in duan[0]:
        if information_new[number][2] == 7:
            B_shihui_len += 1
    for number in duan[8]:
        if information_new[number][2] == 7:
            A_shihui_len += 1
    A_changdu = len(duan[8]) - A_shihui_len
    B_changdu = len(duan[0]) - B_shihui_len
    for number in duan[8]:
        if information_new[number][2] == 7 and information_new[number][1] == 1:  # 车顶：石黑 车身：天空灰
            A_shihui_array.append(number)
        elif information_new[number][2] == 1 and information_new[number][1] == 1:  # 车顶：天空灰 车身：天空灰
            A_tiankonghui.append(number)
        else:
            sys.exit("错21误eq23jfw122ytu")

    A_yu = A_changdu % 5
    B_yu = B_changdu % 5
    flag = 0
    if A_yu != 0 and B_yu != 0:
        flag = 1
        temp = []
        if B_yu == 4:
            duan[8].insert(0, duan[8][-1])
            duan[8].pop(len(duan[8]) - 1)
            temp = duan[8]
        elif B_yu == 3:
            temp.extend(A_tiankonghui[0:2])
            pos1, pos2 = 2, 0
            while pos1 < len(A_tiankonghui) and pos2 < len(A_shihui_array):
                temp.extend(A_shihui_array[pos2:pos2 + 1])
                temp.extend(A_tiankonghui[pos1:pos1 + 5])
                pos1 += 5
                pos2 += 1
            temp.extend(A_shihui_array[pos2:])
            if pos1 < len(A_tiankonghui):
                sys.exit("长度出错jf了akeqwfjl")
        elif B_yu == 2:
            temp.extend(A_tiankonghui[0:3])
            pos1, pos2 = 3, 0
            while pos1 < len(A_tiankonghui) and pos2 < len(A_shihui_array):
                temp.extend(A_shihui_array[pos2:pos2 + 1])
                temp.extend(A_tiankonghui[pos1:pos1 + 5])
                pos1 += 5
                pos2 += 1
            temp.extend(A_shihui_array[pos2:])
            if pos1 < len(A_tiankonghui):
                sys.exit("长度出ewq错了pioakfjl")
        elif B_yu == 1:
            temp.extend(A_tiankonghui[0:4])
            pos1, pos2 = 4, 0
            while pos1 < len(A_tiankonghui) and pos2 < len(A_shihui_array):
                temp.extend(A_shihui_array[pos2:pos2 + 1])
                temp.extend(A_tiankonghui[pos1:pos1 + 5])
                pos1 += 5
                pos2 += 1
            temp.extend(A_shihui_array[pos2:])
            if pos1 < len(A_tiankonghui):
                sys.exit("长度出错了pijf123oakfjl")
        else:
            sys.exit("错误hjWESAD")
        duan[8] = temp
    return flag, duan


def connect_shuijing_tiankonghui(duan, information_new):
    flag1, duan = connect_shuijing_AB(duan, information_new)
    if flag1 == 1:
        flag2, duan = connect_tiankonghui_BA(duan, information_new)
        if flag2 == 1:
            # 交换位置
            # B天空灰B液态灰B乱B闪耀黑A闪耀黑A乱A水晶A天空灰B水晶
            # B天空灰B液态灰B乱B闪耀黑A闪耀黑A乱A水晶B水晶A天空灰
            # B液态灰B乱B闪耀黑A闪耀黑A乱A水晶B水晶A天空灰B天空灰
            # B液态灰B乱B闪耀黑A闪耀黑A乱A水晶B水晶B天空灰A天空灰
            duan.append(deepcopy(duan[1]))
            duan.pop(1)

            duan[7], duan[8] = duan[8], duan[7]

            duan.append(deepcopy(duan[0]))
            duan.pop(0)

            duan[7], duan[8] = duan[8], duan[7]
            return 1
        else:
            return 0
    else:
        return 0


def connect_shuijing_BA(duan, information_new):
    B_shihei_len = 0
    A_shihei_len = 0
    A_shuijing = []
    A_shihei_array = []
    for number in duan[1]:
        if information_new[number][2] == 7:
            B_shihei_len += 1
    for number in duan[7]:
        if information_new[number][2] == 7:
            A_shihei_len += 1
    A_changdu = len(duan[7]) - A_shihei_len
    B_changdu = len(duan[1]) - B_shihei_len
    for number in duan[7]:
        if information_new[number][2] == 7 and information_new[number][1] == 4:  # 车顶：石黑 车身：水晶
            A_shihei_array.append(number)
        elif information_new[number][2] == 4 and information_new[number][1] == 4:  # 车顶：水晶 车身：水晶
            A_shuijing.append(number)
        else:
            sys.exit("错12as误eeqq32w123")
    A_yu = A_changdu % 5
    B_yu = B_changdu % 5
    flag = 0
    if A_yu != 0 and B_yu != 0:
        flag = 1
        temp = []
        if B_yu == 4:
            duan[7].insert(0, duan[7][-1])
            duan[7].pop(len(duan[7]) - 1)
            temp = duan[7]
        elif B_yu == 3:
            temp.extend(A_shuijing[0:2])
            pos1, pos2 = 2, 0
            while pos1 < len(A_shuijing) and pos2 < len(A_shihei_array):
                temp.extend(A_shihei_array[pos2:pos2 + 1])
                temp.extend(A_shuijing[pos1:pos1 + 5])
                pos1 += 5
                pos2 += 1
            temp.extend(A_shihei_array[pos2:])
            if pos1 < len(A_shuijing):
                sys.exit("长度出3错了akf21jl")
        elif B_yu == 2:
            temp.extend(A_shuijing[0:3])
            pos1, pos2 = 3, 0
            while pos1 < len(A_shuijing) and pos2 < len(A_shihei_array):
                temp.extend(A_shihei_array[pos2:pos2 + 1])
                temp.extend(A_shuijing[pos1:pos1 + 5])
                pos1 += 5
                pos2 += 1
            temp.extend(A_shihei_array[pos2:])
            if pos1 < len(A_shuijing):
                sys.exit("长度出错了23pioakf23jl")
        elif B_yu == 1:
            temp.extend(A_shuijing[0:4])
            pos1, pos2 = 4, 0
            while pos1 < len(A_shuijing) and pos2 < len(A_shihei_array):
                temp.extend(A_shihei_array[pos2:pos2 + 1])
                temp.extend(A_shuijing[pos1:pos1 + 5])
                pos1 += 5
                pos2 += 1
            temp.extend(A_shihei_array[pos2:])
            if pos1 < len(A_shuijing):
                sys.exit("长度出31错了pi123oakf321jqwl")
        else:
            sys.exit("错误WE321Seqw12AD123")
        duan[7] = temp
    return flag, duan


def connect_shuijing_AB(duan, information_new):
    A_shihei_len = 0
    B_shihei_len = 0
    B_shuijing = []
    B_shihei_array = []
    for number in duan[1]:
        if information_new[number][2] == 7:
            B_shihei_len += 1
    for number in duan[7]:
        if information_new[number][2] == 7:
            A_shihei_len += 1
    A_changdu = len(duan[7]) - A_shihei_len
    B_changdu = len(duan[1]) - B_shihei_len
    for number in duan[1]:
        if information_new[number][2] == 7 and information_new[number][1] == 4:  # 车顶：石黑 车身：水晶
            B_shihei_array.append(number)
        elif information_new[number][2] == 4 and information_new[number][1] == 4:  # 车顶：水晶 车身：水晶
            B_shuijing.append(number)
        else:
            sys.exit("错12as误eeqq32w123")
    A_yu = A_changdu % 5
    B_yu = B_changdu % 5
    flag = 0
    if A_yu != 0 and B_yu != 0:
        flag = 1
        temp = []
        if A_yu == 4:
            duan[1].insert(0, duan[1][-1])
            duan[1].pop(len(duan[1]) - 1)
            temp = duan[1]
        elif A_yu == 3:
            temp.extend(B_shuijing[0:2])
            pos1, pos2 = 2, 0
            while pos1 < len(B_shuijing) and pos2 < len(B_shihei_array):
                temp.extend(B_shihei_array[pos2:pos2 + 1])
                temp.extend(B_shuijing[pos1:pos1 + 5])
                pos1 += 5
                pos2 += 1
            temp.extend(B_shihei_array[pos2:])
            if pos1 < len(B_shuijing):
                sys.exit("长度出3错了akf21jl")
        elif A_yu == 2:
            temp.extend(B_shuijing[0:3])
            pos1, pos2 = 3, 0
            while pos1 < len(B_shuijing) and pos2 < len(B_shihei_array):
                temp.extend(B_shihei_array[pos2:pos2 + 1])
                temp.extend(B_shuijing[pos1:pos1 + 5])
                pos1 += 5
                pos2 += 1
            temp.extend(B_shihei_array[pos2:])
            if pos1 < len(B_shuijing):
                sys.exit("长度出错了23pioakf23jl")
        elif A_yu == 1:
            temp.extend(B_shuijing[0:4])
            pos1, pos2 = 4, 0
            while pos1 < len(B_shuijing) and pos2 < len(B_shihei_array):
                temp.extend(B_shihei_array[pos2:pos2 + 1])
                temp.extend(B_shuijing[pos1:pos1 + 5])
                pos1 += 5
                pos2 += 1
            temp.extend(B_shihei_array[pos2:])
            if pos1 < len(B_shuijing):
                sys.exit("长度出31错了pi123oakf321jqwl")
        else:
            sys.exit("错误WE321Seqw12AD123")
        duan[1] = temp
    return flag, duan


# 原本是连接是这样的 B天空灰B水晶B液态灰B乱B闪耀黑A闪耀黑A乱A水晶A天空灰
# 情况一：连接方式1：B水晶B液态灰B乱B闪耀黑A闪耀黑A乱A水晶A天空灰B天空灰(在3闪耀黑连接中，再增加这样的连接方法。直接复制过来，虽然很多代码重复了，懒得管了)
# 情况二：连接方式2：B天空灰B液态灰B乱B闪耀黑A闪耀黑A乱A天空灰A水晶B水晶(在3闪耀黑连接中，再增加这样的连接方法。直接复制过来，虽然很多代码重复了，懒得管了)
# 情况三：连接方式3：B液态灰B乱B闪耀黑A闪耀黑A乱A水晶B水晶B天空灰A天空灰(在3闪耀黑连接中，再增加这样的连接方法。直接复制过来，虽然很多代码重复了，懒得管了)
def connect(new_duan, information_new, start, results):
    # 情况一
    duan = deepcopy(new_duan)
    flag, duan = connect_tiankonghui_AB(duan, information_new)
    if flag == 1:
        # 交换位置
        duan.append(deepcopy(duan[0]))
        duan.pop(0)
        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出错了q！p[o-0921")
        results.append(duan)  # 增加一个解
    # 情况二
    duan = deepcopy(new_duan)
    flag, duan = connect_shuijing_AB(duan, information_new)
    if flag == 1:
        # 交换位置
        duan.append(deepcopy(duan[1]))
        duan.pop(1)
        duan[6], duan[7] = duan[7], duan[6]
        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出错了qwepo09211")
        results.append(duan)  # 增加一个解
    # 情况三
    duan = deepcopy(new_duan)
    ans = connect_shuijing_tiankonghui(duan, information_new)
    if ans == 1:
        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出错了q=-0231")
        results.append(duan)  # 增加一个解


def connect2(new_duan, information_new, start, results):
    # 情况一
    duan = deepcopy(new_duan)
    flag, duan = connect_tiankonghui_AB(duan, information_new)
    if flag == 1:
        # 交换位置
        duan.append(deepcopy(duan[0]))
        duan.pop(0)
        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出错了q！p[o-0921")
        results.append(duan)  # 增加一个解
    # 情况二
    duan = deepcopy(new_duan)
    flag, duan = connect_shuijing_AB(duan, information_new)
    if flag == 1:
        # 交换位置
        duan.append(deepcopy(duan[1]))
        duan.pop(1)
        duan[6], duan[7] = duan[7], duan[6]
        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出错了qwepo09211")
        results.append(duan)  # 增加一个解
    # 情况三
    duan = deepcopy(new_duan)
    flag, duan = connect_shanyaohei_AB_ex(duan, information_new)
    if flag == 1:
        # 交换位置
        duan.insert(6, deepcopy(duan[3]))
        duan.pop(3)
        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出错了qwepo09211")
        results.append(duan)  # 增加一个解

    # 情况四
    duan = deepcopy(new_duan)
    ans = connect_shuijing_tiankonghui(duan, information_new)
    if ans == 1:
        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出错了q=-0231")
        results.append(duan)  # 增加一个解

    # 情况五
    duan = deepcopy(new_duan)
    ans = connect_shanyaohei_shuijing(duan, information_new)
    if ans == 1:
        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出错了q=-0231")
        results.append(duan)  # 增加一个解

    # 情况六
    duan = deepcopy(new_duan)
    ans = connect_shanyaohei_tiankonghui(duan, information_new)
    if ans == 1:
        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出错了q=-0231")
        results.append(duan)  # 增加一个解

    # 情况七
    duan = deepcopy(new_duan)
    ans = connect_shanyaohei_tiankonghui_shuijing(duan, information_new)
    if ans == 1:
        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出错了q=-0231")
        results.append(duan)  # 增加一个解


def connect_shanyaohei_tiankonghui_shuijing(duan, information_new):
    flag1, duan = connect_shanyaohei_AB_ex(duan, information_new)
    if flag1 == 1:
        flag2, duan = connect_tiankonghui_BA(duan, information_new)
        if flag2 == 1:
            flag3, duan = connect_shuijing_AB(duan, information_new)
            if flag3 == 1:
                # 原本是连接是这样的 B天空灰B水晶B液态灰B闪耀黑B乱A闪耀黑A乱A水晶A天空灰
                # B水晶B液态灰B闪耀黑B乱A闪耀黑A乱A水晶B天空灰A天空灰
                # B水晶B液态灰B乱A闪耀黑B闪耀黑A乱A水晶B天空灰A天空灰
                # B液态灰B乱A闪耀黑B闪耀黑A乱A水晶B水晶B天空灰A天空灰
                duan.append(deepcopy(duan[0]))
                duan.pop(0)
                duan[7], duan[8] = duan[8], duan[7]

                duan.insert(5, deepcopy(duan[2]))
                duan.pop(2)

                duan.insert(7, deepcopy(duan[0]))
                duan.pop(0)
                return 1

        else:
            return 0
    else:
        return 0


def connect_shanyaohei_tiankonghui(duan, information_new):
    flag1, duan = connect_tiankonghui_AB(duan, information_new)
    if flag1 == 1:
        flag2, duan = connect_shanyaohei_AB_ex(duan, information_new)
        if flag2 == 1:
            # 交换位置
            duan.insert(6, deepcopy(duan[3]))
            duan.pop(3)

            duan.append(deepcopy(duan[0]))
            duan.pop(0)
            return 1
        else:
            return 0
    else:
        return 0


def connect_shanyaohei_shuijing(duan, information_new):
    flag1, duan = connect_shuijing_AB(duan, information_new)
    if flag1 == 1:
        flag2, duan = connect_shanyaohei_AB_ex(duan, information_new)
        if flag2 == 1:
            # 交换位置
            duan.insert(6, deepcopy(duan[3]))
            duan.pop(3)

            duan.insert(8, deepcopy(duan[1]))
            duan.pop(1)
            return 1
        else:
            return 0
    else:
        return 0


def connect_shuijing_shanyaohei(duan, information_new):
    flag1, duan = connect_shuijing_AB(duan, information_new)
    if flag1 == 1:
        flag2, duan = connect_shanyaohei_BA(duan, information_new)
        if flag2 == 1:
            # 交换位置
            # B天空灰B水晶B液态灰B闪耀黑B乱A乱A闪耀黑A水晶A天空灰
            # B天空灰B液态灰B闪耀黑B乱A乱A闪耀黑A水晶A天空灰B水晶
            # B天空灰B液态灰B闪耀黑B乱A乱A闪耀黑A水晶B水晶A天空灰
            # B天空灰B液态灰B乱A乱A闪耀黑A水晶B水晶A天空灰B闪耀黑
            # B天空灰B液态灰B乱A乱A水晶B水晶A天空灰B闪耀黑A闪耀黑
            # B天空灰B液态灰B乱A乱A水晶A天空灰B水晶B闪耀黑A闪耀黑
            # B天空灰B液态灰B乱A乱A天空灰A水晶B水晶B闪耀黑A闪耀黑
            duan.append(deepcopy(duan[1]))
            duan.pop(1)

            duan[7], duan[8] = duan[8], duan[7]

            duan.append(deepcopy(duan[2]))
            duan.pop(2)

            duan.append(deepcopy(duan[4]))
            duan.pop(4)

            duan[5], duan[6] = duan[6], duan[5]

            duan[4], duan[5] = duan[5], duan[4]
            return 1
        else:
            return 0
    else:
        return 0


# # 情况六：连接方式6：B水晶B液态灰B乱A乱A水晶A天空灰B天空灰B闪耀黑A闪耀黑
def connect_tiankonghui_shanyaohei(duan, information_new):
    flag1, duan = connect_tiankonghui_AB(duan, information_new)
    if flag1 == 1:
        flag2, duan = connect_shanyaohei_BA(duan, information_new)
        if flag2 == 1:
            # B天空灰B水晶B液态灰B闪耀黑B乱A乱A闪耀黑A水晶A天空灰
            # B水晶B液态灰B闪耀黑B乱A乱A闪耀黑A水晶A天空灰B天空灰
            # B水晶B液态灰B乱A乱A闪耀黑A水晶A天空灰B天空灰B闪耀黑
            # B水晶B液态灰B乱A乱A水晶A天空灰B天空灰B闪耀黑A闪耀黑
            # 交换位置
            duan.append(deepcopy(duan[0]))
            duan.pop(0)

            duan.append(deepcopy(duan[2]))
            duan.pop(2)

            duan.append(deepcopy(duan[4]))
            duan.pop(4)
            return 1
        else:
            return 0
    else:
        return 0


# # 情况七：连接方式7：B液态灰B乱A乱A天空灰B天空灰B闪耀黑A闪耀黑A水晶B水晶
def connect_tiankonghui_shanyaohei_shuijing(duan, information_new):
    flag1, duan = connect_tiankonghui_AB(duan, information_new)
    if flag1 == 1:
        flag2, duan = connect_shanyaohei_BA(duan, information_new)
        if flag2 == 1:
            flag3, duan = connect_shuijing_AB(duan, information_new)
            if flag3 == 1:
                # B天空灰B水晶B液态灰B闪耀黑B乱A乱A闪耀黑A水晶A天空灰
                # B水晶B液态灰B闪耀黑B乱A乱A闪耀黑A水晶A天空灰B天空灰
                # B水晶B液态灰B乱A乱A闪耀黑A水晶A天空灰B天空灰B闪耀黑
                # B水晶B液态灰B乱A乱A水晶A天空灰B天空灰B闪耀黑A闪耀黑
                # B水晶B液态灰B乱A乱A天空灰B天空灰B闪耀黑A闪耀黑A水晶
                # B液态灰B乱A乱A天空灰B天空灰B闪耀黑A闪耀黑A水晶B水晶
                # 交换位置
                duan.append(deepcopy(duan[0]))
                duan.pop(0)

                duan.append(deepcopy(duan[2]))
                duan.pop(2)

                duan.append(deepcopy(duan[4]))
                duan.pop(4)

                duan.append(deepcopy(duan[4]))
                duan.pop(4)

                duan.append(deepcopy(duan[0]))
                duan.pop(0)
                return 1

        else:
            return 0
    else:
        return 0


# 原本是连接是这样的 B天空灰B水晶B液态灰B闪耀黑B乱A乱A闪耀黑A水晶A天空灰
# 情况一：连接方式1：B水晶B液态灰B闪耀黑B乱A乱A闪耀黑A水晶A天空灰B天空灰
# 情况二：连接方式2：B天空灰B液态灰B闪耀黑B乱A乱A闪耀黑A天空灰A水晶B水晶
# 情况三：连接方式3：B天空灰B水晶B液态灰B乱A乱A天空灰A水晶A闪耀黑B闪耀黑

# 情况四：连接方式4：B液态灰B闪耀黑B乱A乱A闪耀黑A水晶B水晶B天空灰A天空灰
# 情况五：连接方式5：B天空灰B液态灰B乱A乱A天空灰A水晶B水晶B闪耀黑A闪耀黑
# 情况六：连接方式6：B水晶B液态灰B乱A乱A水晶A天空灰B天空灰B闪耀黑A闪耀黑

# 情况七：连接方式7：B液态灰B乱A乱A天空灰B天空灰B闪耀黑A闪耀黑A水晶B水晶
def connect_other(new_duan, information_new, start, results):
    # 情况一
    duan = deepcopy(new_duan)
    flag, duan = connect_tiankonghui_AB(duan, information_new)
    if flag == 1:
        # 交换位置
        duan.append(deepcopy(duan[0]))
        duan.pop(0)
        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出错了q！p[o-0921")
        results.append(duan)  # 增加一个解
    # 情况二
    duan = deepcopy(new_duan)
    flag, duan = connect_shuijing_AB(duan, information_new)
    if flag == 1:
        # 交换位置
        duan.append(deepcopy(duan[1]))
        duan.pop(1)
        duan[6], duan[7] = duan[7], duan[6]
        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出错了qwepo09211")
        results.append(duan)  # 增加一个解
    # 情况三
    duan = deepcopy(new_duan)
    flag, duan = connect_shanyaohei_AB(duan, information_new)
    if flag == 1:
        # 交换位置
        duan[6], duan[8] = duan[8], duan[6]
        duan.append(deepcopy(duan[3]))
        duan.pop(3)
        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出错了qwepo09211")
        results.append(duan)  # 增加一个解

    # 情况四
    duan = deepcopy(new_duan)
    ans = connect_shuijing_tiankonghui(duan, information_new)
    if ans == 1:
        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出错了q=-0231")
        results.append(duan)  # 增加一个解

    # 情况五
    duan = deepcopy(new_duan)
    ans = connect_shuijing_shanyaohei(duan, information_new)
    if ans == 1:
        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出错了q=-0231")
        results.append(duan)  # 增加一个解

    # 情况六
    duan = deepcopy(new_duan)
    ans = connect_tiankonghui_shanyaohei(duan, information_new)
    if ans == 1:
        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出错了q=-0231")
        results.append(duan)  # 增加一个解

    # 情况七
    duan = deepcopy(new_duan)
    ans = connect_tiankonghui_shanyaohei_shuijing(duan, information_new)
    if ans == 1:
        seq = convert_two_to_one(duan)
        if check_solution(seq, start) != 1:
            sys.exit("序列出错了q=-0231")
        results.append(duan)  # 增加一个解


# 原本是连接是这样的 B天空灰B水晶B液态灰B闪耀黑B乱A闪耀黑A乱A水晶A天空灰
def connect_shanyaohei_AB_ex(duan, information_new):
    B_siqu_len = 0
    B_erqu_array = []
    B_siqu_array = []
    B_shihei_array = []
    for number in duan[3]:
        if information_new[number][2] == 7 and information_new[number][1] == 6:  # 车顶：石黑 车身：闪耀黑
            B_shihei_array.append(number)
        elif information_new[number][3] == 1:
            B_siqu_array.append(number)
            B_siqu_len += 1
        elif information_new[number][3] == 0:
            B_erqu_array.append(number)
        else:
            sys.exit("错eqw64312uy")
    shihei_flag = len(B_shihei_array)
    A_changdu = len(duan[5])
    B_changdu = len(duan[3]) - shihei_flag

    A_yu = A_changdu % 5
    B_yu = B_changdu % 5
    flag = 0
    if A_yu != 0 and B_yu != 0:
        flag = 1
        if A_yu == 4:
            # 插入一个二驱车到最前面
            duan[3].insert(0, duan[3][-2])
            duan[3].pop(len(duan[3]) - 2)
        elif A_yu == 3:
            # 插入两个二驱车到最前面
            duan[3].insert(0, duan[3][-2])
            duan[3].insert(0, duan[3][-3])
            duan[3].pop(len(duan[3]) - 2)
            duan[3].pop(len(duan[3]) - 2)
        elif A_yu == 2:
            # 插入三个二驱车到最前面
            duan[3].insert(0, duan[3][-2])
            duan[3].insert(0, duan[3][-3])
            duan[3].insert(0, duan[3][-4])
            duan[3].pop(len(duan[3]) - 2)
            duan[3].pop(len(duan[3]) - 2)
            duan[3].pop(len(duan[3]) - 2)
        elif A_yu == 1:
            # 插入四个二驱车到最前面
            duan[3].insert(0, duan[3][-2])
            duan[3].insert(0, duan[3][-3])
            duan[3].insert(0, duan[3][-4])
            duan[3].insert(0, duan[3][-5])
            duan[3].pop(len(duan[3]) - 2)
            duan[3].pop(len(duan[3]) - 2)
            duan[3].pop(len(duan[3]) - 2)
            duan[3].pop(len(duan[3]) - 2)
        else:
            sys.exit("错213误的312复苏与人体qw12123")
    return flag, duan


# 原本是连接是这样的 B天空灰B水晶B液态灰B闪耀黑B乱A乱A闪耀黑A水晶A天空灰
def connect_shanyaohei_AB(duan, information_new):
    B_siqu_len = 0
    B_erqu_array = []
    B_siqu_array = []
    B_shihei_array = []
    for number in duan[3]:
        if information_new[number][2] == 7 and information_new[number][1] == 6:  # 车顶：石黑 车身：闪耀黑
            B_shihei_array.append(number)
        elif information_new[number][3] == 1:
            B_siqu_array.append(number)
            B_siqu_len += 1
        elif information_new[number][3] == 0:
            B_erqu_array.append(number)
        else:
            sys.exit("错eqw64312uy")
    shihei_flag = len(B_shihei_array)
    A_changdu = len(duan[6])
    B_changdu = len(duan[3]) - shihei_flag

    A_yu = A_changdu % 5
    B_yu = B_changdu % 5
    flag = 0
    if A_yu != 0 and B_yu != 0:
        flag = 1
        if A_yu == 4:
            # 插入一个二驱车到最前面
            duan[3].insert(0, duan[3][-2])
            duan[3].pop(len(duan[3]) - 2)
        elif A_yu == 3:
            # 插入两个二驱车到最前面
            duan[3].insert(0, duan[3][-2])
            duan[3].insert(0, duan[3][-3])
            duan[3].pop(len(duan[3]) - 2)
            duan[3].pop(len(duan[3]) - 2)
        elif A_yu == 2:
            # 插入三个二驱车到最前面
            duan[3].insert(0, duan[3][-2])
            duan[3].insert(0, duan[3][-3])
            duan[3].insert(0, duan[3][-4])
            duan[3].pop(len(duan[3]) - 2)
            duan[3].pop(len(duan[3]) - 2)
            duan[3].pop(len(duan[3]) - 2)
        elif A_yu == 1:
            # 插入四个二驱车到最前面
            duan[3].insert(0, duan[3][-2])
            duan[3].insert(0, duan[3][-3])
            duan[3].insert(0, duan[3][-4])
            duan[3].insert(0, duan[3][-5])
            duan[3].pop(len(duan[3]) - 2)
            duan[3].pop(len(duan[3]) - 2)
            duan[3].pop(len(duan[3]) - 2)
            duan[3].pop(len(duan[3]) - 2)
        else:
            sys.exit("错213误的312复苏与人体qw12123")
    return flag, duan


# 原本是连接是这样的 B天空灰B水晶B液态灰B闪耀黑B乱A乱A闪耀黑A水晶A天空灰
def connect_shanyaohei_BA(duan, information_new):
    B_siqu_len = 0
    B_erqu_array = []
    B_siqu_array = []
    B_shihei_array = []
    for number in duan[3]:
        if information_new[number][2] == 7 and information_new[number][1] == 6:  # 车顶：石黑 车身：闪耀黑
            B_shihei_array.append(number)
        elif information_new[number][3] == 1:
            B_siqu_array.append(number)
            B_siqu_len += 1
        elif information_new[number][3] == 0:
            B_erqu_array.append(number)
        else:
            sys.exit("错eqw64312uy")
    shihei_flag = len(B_shihei_array)
    A_changdu = len(duan[6])
    B_changdu = len(duan[3]) - shihei_flag

    A_yu = A_changdu % 5
    B_yu = B_changdu % 5
    flag = 0
    if A_yu != 0 and B_yu != 0:
        flag = 1
    return flag, duan

# # 当出现A乱和B乱各自多了一个四驱车时，需要另外考虑连接方式
# # 原本是连接是这样的 B天空灰B水晶B液态灰B闪耀黑B乱A乱A闪耀黑A水晶A天空灰
# # 情况一：连接方式1：B天空灰B水晶B液态灰B乱A乱A水晶A天空灰A闪耀黑B闪耀黑(在3闪耀黑连接中，再增加这样的连接方法。直接复制过来，虽然很多代码重复了，懒得管了)
# # 情况一：连接方式2：B水晶B液态灰B闪耀黑B乱A乱A闪耀黑A水晶A天空灰B天空灰(在3闪耀黑连接中，再增加这样的连接方法。直接复制过来，虽然很多代码重复了，懒得管了)
# # 情况二：连接方式3：B天空灰B液态灰B闪耀黑B乱A乱A闪耀黑A天空灰A水晶B水晶(在3闪耀黑连接中，再增加这样的连接方法。直接复制过来，虽然很多代码重复了，懒得管了)
# # 情况三：连接方式4：B液态灰B乱A乱A水晶B水晶B天空灰A天空灰A闪耀黑B闪耀黑(在3闪耀黑连接中，再增加这样的连接方法。直接复制过来，虽然很多代码重复了，懒得管了)
# def connect_other(new_duan, information_new, start, results):
#     # 情况一
#     duan = deepcopy(new_duan)
#     flag, duan = connect_tiankonghui_AB(duan, information_new)
#     if flag == 1:
#         # 交换位置
#         duan.append(deepcopy(duan[0]))
#         duan.pop(0)
#         seq = convert_two_to_one(duan)
#         if check_solution(seq, start) != 1:
#             sys.exit("序列出错了q！p[o-0921")
#         results.append(duan)  # 增加一个解
#     # 情况二
#     duan = deepcopy(new_duan)
#     flag, duan = connect_shuijing_AB(duan, information_new)
#     if flag == 1:
#         # 交换位置
#         duan.append(deepcopy(duan[1]))
#         duan.pop(1)
#         duan[6], duan[7] = duan[7], duan[6]
#         seq = convert_two_to_one(duan)
#         if check_solution(seq, start) != 1:
#             sys.exit("序列出错了qwepo09211")
#         results.append(duan)  # 增加一个解
#     # 情况三
#     duan = deepcopy(new_duan)
#     ans = connect_shuijing_tiankonghui(duan, information_new)
#     if ans == 1:
#         seq = convert_two_to_one(duan)
#         if check_solution(seq, start) != 1:
#             sys.exit("序列出错了q=-0231")
#         results.append(duan)  # 增加一个解
