import os
import numpy as np


def transf(str):
    if str == "A":
        return 0
    elif str == "B":
        return 1
    elif str == "C":
        return 2
    elif str == "D":
        return 3
    elif str == "E":
        return 4
    else:
        print("debug in transf:")
        os.system("pause")


def judgeway(chess, lset, nset):
    set = np.where(chessboard == chess)
    chessboard[nset][lset] = chess
    chessboard[int(set[0])][int(set[1])] = 0
    tem_chessboard.append(np.copy(chessboard))
    # print(chessboard)
    # classic way -> [0,17]
    # chess / abs(chess) = chess_sign
    if set[0] - (chess / abs(chess)) == nset and set[1] == lset:
        return [(chess / abs(chess)) * ((abs(chess) - 1) * 3), chess / abs(chess)]
    elif set[0] == nset and set[1] - (chess / abs(chess)) == lset:
        return [(chess / abs(chess)) * ((abs(chess) - 1) * 3 + 2), chess / abs(chess)]
    elif set[0] - (chess / abs(chess)) == nset and set[1] - (chess / abs(chess)) == lset:
        return [(chess / abs(chess)) * ((abs(chess) - 1) * 3 + 1), chess / abs(chess)]
    else:
        print("debug in judgeway:")
        os.system("pause")


# def movechess(cb, step, chessman_sign):
# def movechess(cb, step, chessman_sign):
#     if step == 0:
#         tem = np.where(cb == chessman_sign)
#     else :
#         tem = np.where(cb == chessman_sign * ((abs(step) - (abs(step) % 3)) / 3 + 1))
#     # first if to find only one way
#     if tem[0] or tem[1] or tem[0] == 0:
#         if abs(step) % 3 == 0:
#             if 5 > int(tem[0]) - chessman_sign >= 0:
#                 cb[int(tem[0]) - int(chessman_sign)][int(tem[1])] = chessman_sign \
#                     * ((abs(step) - (abs(step) % 3)) / 3 + 1)
#                 cb[int(tem[0])][int(tem[1])] = 0
#             else:
#                 cb = np.zeros_like(cb)
#         elif abs(step) % 3 == 1:
#             if 5 > int(tem[0]) - chessman_sign >= 0 and 5 > int(tem[1]) - chessman_sign >= 0:
#                 cb[int(tem[0]) - int(chessman_sign)][int(tem[1]) - int(chessman_sign)] = chessman_sign \
#                     * ((abs(step) - (abs(step) % 3)) / 3 + 1)
#                 cb[int(tem[0])][int(tem[1])] = 0
#             else:
#                 cb = np.zeros_like(cb)
#         else:
#             if 5 > int(tem[1]) - chessman_sign >= 0:
#                 cb[int(tem[0])][int(tem[1]) - int(chessman_sign)] = chessman_sign * (
#                         (abs(step) - (abs(step) % 3)) / 3 + 1)
#                 cb[int(tem[0])][int(tem[1])] = 0
#             else:
#                 cb = np.zeros_like(cb)
#     else:
#         print("debug in movechess")
#         os.system("pause")
#     return np.copy(cb)
#
#
# def step_to_data(early_chessboard, dice, step, chessman_sign):
#     early = False
#     lately = False
#     # print(process.index([str(dice), step]))
#     if dice != ((abs(step) - (abs(step) % 3)) / 3 + 1):
#         if dice < ((abs(step) - (abs(step) % 3)) / 3 + 1):
#             for x in range(dice - 1, 0, -1):
#                 ts = np.where(early_chessboard == x * chessman_sign)
#                 if ts[0] or ts[1] or ts[0] == 0:
#                     early = True
#                     rt = [movechess(np.copy(early_chessboard), (x - 1) * 3 * chessman_sign, chessman_sign),
#                           movechess(np.copy(early_chessboard), ((x - 1) * 3 + 1) * chessman_sign, chessman_sign),
#                           movechess(np.copy(early_chessboard), ((x - 1) * 3 + 2) * chessman_sign, chessman_sign)]
#                     break
#             if not early:
#                 rt = [np.zeros_like(early_chessboard), np.zeros_like(early_chessboard), np.zeros_like(early_chessboard)]
#
#             rt.append(movechess(np.copy(early_chessboard), chessman_sign * (abs(step) - (abs(step) % 3)), chessman_sign))
#             rt.append(movechess(np.copy(early_chessboard), chessman_sign * (abs(step) - (abs(step) % 3) + 1), chessman_sign))
#             rt.append(movechess(np.copy(early_chessboard), chessman_sign * (abs(step) - (abs(step) % 3) + 2), chessman_sign))
#             return [(3 + abs(step) % 3), rt]
#         else:
#             rt = [movechess(np.copy(early_chessboard), chessman_sign * (abs(step) - (abs(step) % 3)), chessman_sign),
#                   movechess(np.copy(early_chessboard), chessman_sign * (abs(step) - (abs(step) % 3) + 1), chessman_sign),
#                   movechess(np.copy(early_chessboard), chessman_sign * (abs(step) - (abs(step) % 3) + 2), chessman_sign)]
#             #
#             for x in range(dice + 1, 7):
#                 ts = np.where(early_chessboard == x * chessman_sign)
#                 if ts[0] or ts[1] or ts[0] == 0:
#                     lately = True
#                     rt.append(movechess(np.copy(early_chessboard), (x - 1) * 3 * chessman_sign, chessman_sign))
#                     rt.append(movechess(np.copy(early_chessboard), ((x - 1) * 3 + 1) * chessman_sign, chessman_sign))
#                     rt.append(movechess(np.copy(early_chessboard), ((x - 1) * 3 + 2) * chessman_sign, chessman_sign))
#                     break
#             if not lately:
#                 rt.append(np.zeros_like(early_chessboard))
#                 rt.append(np.zeros_like(early_chessboard))
#                 rt.append(np.zeros_like(early_chessboard))
#             return [(abs(step) % 3), rt]
#     else:
#         rt = [movechess(np.copy(early_chessboard), chessman_sign * (abs(step) - (abs(step) % 3)), chessman_sign)]
#         rt.append(movechess(np.copy(early_chessboard), chessman_sign * (abs(step) - (abs(step) % 3) + 1), chessman_sign))
#         rt.append(movechess(early_chessboard, chessman_sign * (abs(step) - (abs(step) % 3) + 2), chessman_sign))
#         rt.append(np.zeros_like(early_chessboard))
#         rt.append(np.zeros_like(early_chessboard))
#         rt.append(np.zeros_like(early_chessboard))
#         return [(abs(step) % 3), rt]

def movechessman(cb, step, chessman_sign):
    if step == 0:
        tem = np.where(cb == chessman_sign)
    else :
        tem = np.where(cb == chessman_sign * ((abs(step) - (abs(step) % 3)) / 3 + 1))
    # first if to find only one way
    if tem[0] or tem[1] or tem[0] == 0:
        if abs(step) % 3 == 0:
            if 5 > int(tem[0]) - chessman_sign >= 0:
                cb = np.zeros_like(cb)
                cb[int(tem[0])][int(tem[1])] = 1
            else:
                cb = np.zeros_like(cb)

        elif abs(step) % 3 == 1:
            if 5 > int(tem[0]) - chessman_sign >= 0 and 5 > int(tem[1]) - chessman_sign >= 0:
                cb = np.zeros_like(cb)
                cb[int(tem[0])][int(tem[1])] = 1
            else:
                cb = np.zeros_like(cb)

        else:
            if 5 > int(tem[1]) - chessman_sign >= 0:
                cb = np.zeros_like(cb)
                cb[int(tem[0])][int(tem[1])] = 1
            else:
                cb = np.zeros_like(cb)

    else:
        print("debug in movechess")
        os.system("pause")
    return np.copy(cb)

def step_to_chessman(early_chessboard, dice, step, chessman_sign):
    early = False
    lately = False
    # print(process.index([str(dice), step]))
    if dice != ((abs(step) - (abs(step) % 3)) / 3 + 1):
        if dice < ((abs(step) - (abs(step) % 3)) / 3 + 1):
            for x in range(dice - 1, 0, -1):
                ts = np.where(early_chessboard == x * chessman_sign)
                if ts[0] or ts[1] or ts[0] == 0:
                    early = True
                    rt = [movechessman(np.copy(early_chessboard), (x - 1) * 3 * chessman_sign, chessman_sign)]
                    break
            if not early:
                rt = [np.zeros_like(early_chessboard), np.zeros_like(early_chessboard), np.zeros_like(early_chessboard)]
            rt.append(movechessman(np.copy(early_chessboard), chessman_sign * (abs(step) - (abs(step) % 3)), chessman_sign))
            return [(3 + abs(step) % 3), rt]
        else:
            rt = [movechessman(np.copy(early_chessboard), chessman_sign * (abs(step) - (abs(step) % 3)), chessman_sign)]
            #
            for x in range(dice + 1, 7):
                ts = np.where(early_chessboard == x * chessman_sign)
                if ts[0] or ts[1] or ts[0] == 0:
                    lately = True
                    rt.append(movechessman(np.copy(early_chessboard), (x - 1) * 3 * chessman_sign, chessman_sign))
                    break
            if not lately:
                rt.append(np.zeros_like(early_chessboard))
            return [(abs(step) % 3), rt]
    else:
        rt = [movechessman(np.copy(early_chessboard), chessman_sign * (abs(step) - (abs(step) % 3)), chessman_sign)]
        rt.append(np.zeros_like(early_chessboard))
        return [(abs(step) % 3), rt]


# script's start
path = ".//dataset/"
savepath = ".///"
# put file's name in box
box = os.listdir(path)

for b in box:
    f_tem = open(path + b, "r", encoding='utf-8')
    r_tem = f_tem.readlines()
    for line in r_tem:
        # every line to format
        # first line is red chess set
        # second line is blue chess set
        # create a set to save steps in a game, in else segment , add other steps to list
        if r_tem.index(line) == 0:
            R_C = line
        elif r_tem.index(line) == 1:
            B_C = line
        elif r_tem.index(line) == 2:
            steps = [line]
        else:
            steps.append(line)

    # 棋盘的初始化
    chessboard = np.zeros([5, 5], dtype=int)

    # split using ";", because every chess set split by ";"
    R_C = R_C.split(";")
    B_C = B_C.split(";")
    # set chess to the chessboard
    for step in R_C:
        step = step.replace('\n', "")
        # chessboard-A5  ->  chessboard[5-5][transfer(A)]
        # chessboard[][]-1  <-  red-sign * int("1“)
        chessboard[5 - int(step[-3])][transf(step[-4])] = -1 * int(step[-1])

    for step in B_C:
        step = step.replace('\n', "")
        chessboard[5 - int(step[-3])][transf(step[-4])] = int(step[-1])

    # initial chessboard
    tem_chessboard = [np.copy(chessboard)]
    # steps的规范化输出
    for step in steps:
        # judge this step is reg or blue
        if step[-7] == "R":
            chess_sign = -1
        else:
            chess_sign = 1

            print(step[-6], step[-4], step[-3])
        if steps.index(step) == 0:
            process = [[step[-10], judgeway(chess_sign * int(step[-6]), transf(step[-4]), 5 - int(step[-3]))]]
        else:
            process.append([step[-10], judgeway(chess_sign * int(step[-6]), transf(step[-4]), 5 - int(step[-3]))])
    #print(tem_chessboard)
    # print(process)

    # s = 0
    # for step in process:
    #     if s % 2 == 0:
    #         # 胜利方的step作为数据集收录（注:棋盘规范化，胜利AI化）
    #         if process.index(step) == 0:
    #             TSetOData = [step_to_data(tem_chessboard[s], int(step[0]), int(step[1][0]), int(step[1][1]))]
    #         else:
    #             TSetOData.append(step_to_data(tem_chessboard[s], int(step[0]), int(step[1][0]), int(step[1][1])))
    #     s += 1
    # s = 0

    s = 0
    for step in process:
        if s%2==0:
            # 胜利方的step作为数据集收录（注:棋盘规范化，胜利AI化）
            if process.index(step) == 0:
                TOData = [step_to_chessman(tem_chessboard[s], int(step[0]), int(step[1][0]), int(step[1][1]))]
            else:
                TOData.append(step_to_chessman(tem_chessboard[s], int(step[0]), int(step[1][0]), int(step[1][1])))
        s+=1
    s=0


    # for step in range(7):
    #     s_tem = open(savepath + "已转换" + str(s) + str(b), "w+", encoding='utf-8')
    #     for x in range(5):
    #         for y in range(5):
    #             if(tem_chessboard[step][x][y] > 0):
    #                 s_tem.write(str(tem_chessboard[step][x][y])+ " ")
    #             else:
    #                 s_tem.write(str(0)+ " ")
    #         s_tem.write('\n')
    #
    #     for x in range(5):
    #         for y in range(5):
    #             if(tem_chessboard[step][x][y] < 0):
    #                 s_tem.write(str(-1*tem_chessboard[step][x][y])+ " ")
    #             else:
    #                 s_tem.write(str(0)+ " ")
    #         s_tem.write('\n')
    #     s+=1
    #     s_tem.close()
    z = 0
    s = 0
    for step in TOData:
        s_tem = open(savepath + "已转换" + str(s) + str(b), "w+", encoding='utf-8')
        # out
        s_tem.write(str(step[0]) + '\n')
        # chess statement

        for x in range(5):
            for y in range(5):
                if(tem_chessboard[z][x][y] > 0):
                    s_tem.write(str(tem_chessboard[z][x][y])+ " ")
                else:
                    s_tem.write(str(0)+ " ")
            s_tem.write('\n')

        for x in range(5):
            for y in range(5):
                if(tem_chessboard[z][x][y] < 0):
                    s_tem.write(str(-1*tem_chessboard[z][x][y])+ " ")
                else:
                    s_tem.write(str(0)+ " ")
            s_tem.write('\n')
        z+=2


        step[1][0] += step[1][1]

        for x in range(5):
            for y in range(5):
                s_tem.write(str(step[1][0][x][y]) + " ")
            s_tem.write('\n')
        s += 1
        s_tem.close()




    #
    # for step in TSetOData:
    #     s_tem = open(savepath + "已转换" + str(s) + str(b), "w+", encoding='utf-8')
    #     #s_tem.write(str(step[0]) + '\n')
    #     #s_tem.write(str(dice) + '\n')
    #     for x in range(5):
    #         for y in range(5):
    #             s_tem.write(str(step[1][0][x][y]) + " ")
    #         s_tem.write('\n')
    #     s += 1
    #     s_tem.close()
