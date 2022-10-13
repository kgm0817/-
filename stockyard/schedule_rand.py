from generator import generator
from evaluate import evaluate
import pandas as pd
import random
import numpy as np
import copy
import matplotlib.pyplot as plt
from scipy import stats
from util import order
from datetime import datetime
from datetime import timedelta
from util import dfs


pd.set_option('display.max_rows', 500)

SEED = 3
random.seed(SEED)
np.random.seed(SEED)
# numpy 옵션
np.set_printoptions(threshold=np.inf, linewidth=np.inf)

params = [30, 30, 3, 7, 0, 10, 10]
flag = [True, True, True, True]

map, df = generator(params, flag)

df_len, _ = df.shape
allow_time = [random.randrange(20, 40) for _ in range(df_len)]

allow_df = copy.deepcopy(df)
allow_df['allow_time'] = allow_time
print(allow_df)


# include_in = include_time(allow_df, 30)
include_in = include_or_time(allow_df)
print(include_in)
print(len(include_in))

schedule_index_list = [i for i in range(df_len)]
print(schedule_index_list)

random_schedule = [random.choice(i) for i in include_in]
print(random_schedule)

avail_schedule = check_schedule(random_schedule, include_in, allow_df)


# for i in include_in:
#     for j in i:
#         select_index_list.append(j)
#
# select_index_list = []
# for i in range(len(include_in)):
#     for j in include_in[i]:

# i = 0
# while i < len(include_in):
#     select_index_list = []
#     print(include_in[i][0])
#     i += 1
#     for z in include_in[i]:
#         for asdf in
#         select_index_list.append(z)
#
# print(select_index_list)


# schedule_dfs = []
# for i, j in enumerate(include_in):
#     temp = []
#     # j.remove(i)
#     for k in j:
#         temp.append(k - 1)
#     schedule_dfs.append(temp)
#
# print(schedule_dfs)


# for i, j in enumerate(include_in):
#     select_index_list = []
#     level_list = []
#     for a in j:
#         level_list.append(i)
#         for b in a:
#
#     print(select_index_list)
# print(select_index_list)
# input()
# select_index_list = []
# level_list = []

# while level_list:
bit_list = copy.deepcopy(include_in)
for i in bit_list:
    for j, k in enumerate(i):
        i[j] = 0
print(bit_list)

visit_list = []
for i in bit_list:
    visit_list.append(i.index(0))
    i[i.index(0)] = 1

print(visit_list)
current_list = []
for i, j in enumerate(visit_list):
    current_list.append(include_in[i][j])
print(current_list)
print(bit_list)

for i in range(len(bit_list)-1, 0, -1):
    visit_list[i] = bit_list[i].index(0)
    bit_list[i][bit_list[i].index(0)] = 1
    print(visit_list)
    print(bit_list)
    input()
print(bit_list)

# while True:
#     for i in bit_list:
#         i.index(0)

input()

schedule_dict = dfs.include_dict(include_in)
print(schedule_dict)
aaa = dfs.dfs(schedule_dict, 0)
print(aaa)




# process_num = len(include_in)
# print(process_num)
# i = 0
# select_index_list = []
# possible = False
# one_choice = []
# while i < process_num-1:
#     print(i)
#     if possible:
#         i += 1
#     copy_include_in = copy.deepcopy(include_in)
#     select_index = random.choice(include_in[i])
#     print('select_index', select_index)
#
#     if len(include_in[i]) == 1:
#         possible = True
#         print(copy_include_in)
#         for k in copy_include_in[i+1:]:
#             if select_index in k:
#                 k.remove(select_index)
#         include_in = copy_include_in
#         print(copy_include_in)
#         select_index_list.append(select_index)
#         continue
#
#     print(copy_include_in)
#     for k in copy_include_in[i+1:]:
#         if select_index in k:
#             k.remove(select_index)
#
#     for k in copy_include_in[i+1:]:
#         if len(k) <= 1:
#             one_choice.append(k[0])
#             possible = False
#             # if k in include_in[i]:
#             #
#             #     possible = True
#             print('continue')
#             break
#         else:
#             possible = True
#
#     print(possible)
#     print(copy_include_in)
#
#     if possible:
#         include_in = copy_include_in
#         select_index_list.append(select_index)
#     print(select_index_list)
#     input()

# while i < process_num-1:
#     print('\n\n',select_index_list)
#     print(i)
#     if possible:
#         i += 1
#     copy_include_in = copy.deepcopy(include_in)
#     select_index = random.choice(include_in[i])
#     print('select_index', select_index)
#     print(copy_include_in)
#
#     for k in copy_include_in[i+1:]:
#         if select_index in k:
#             k.remove(select_index)
#     print(copy_include_in)
#     possible = True
#     cc = []
#     for k in copy_include_in[i+1:]:
#         if len(k) == 1:
#           cc.append(k[0])
#
#     if len(cc) != len(set(cc)):
#         possible = False
#         print('asdfasdf')
#         input()
#         continue
#
#     vvv = copy.deepcopy(copy_include_in)
#     for k in vvv[i+1:]:
#         if not len(k) == 1:
#             for z in cc:
#                 if z in k:
#                     k.remove(z)
#             # print(k)
#             # input()
#             if len(k) == 1:
#                 cc
#             if len(k) == 0:
#                 possible = False
#                 print('zzzz')
#                 break
#     선택한거 제거 -> 하나짜리가 남는다 -> 하나끼리 중복 확인
#     하나 한거 제거 -> 하나 짜리가 남는다 -> 하나끼리 중복확인
#     하나 짜리가 없을때까지
#
#     for k in copy_include_in[i+1:]:
#         if select_index in k:
#             k.remove(select_index)
#
#     for k in copy_include_in[i+1:]:
#         if len(k) == 1:
#           cc.append(k[0])
#
#     if possible:
#         include_in = copy_include_in
#         select_index_list.append(select_index)
#     else:
#         pass
#     print('111111111')
#     input()




# print(new_schedule)
# print(len(new_schedule))


# schedule_in = df[df.type == 1].reset_index(drop=True)
# schedule_out = df[df.type == 2].reset_index(drop=True)
# # print(schedule_in)
#
# include_in = include_time(schedule_in, 30)
# print(include_in)


# # 스케줄 복사
# df_copy = copy.deepcopy(new_df)
#
# # 맵 복사
# new_map_copy = copy.deepcopy(new_map)
#
# x_axis, y_axis = order.order(df_copy)
#
#
# #plot
# x_axis_list_str = list(map(str, x_axis))
# x_index_list = [i for i,j in enumerate(x_axis)]
# # print(x_index_list)
# plt.plot(x_axis_list_str, y_axis, 'ok')
# helper = np.arange(len(x_axis_list_str))
# # helper1 = np.arange(len(y_axis_list_str))
# plt.xticks(ticks=helper, labels=x_axis_list_str)
# # plt.yticks(ticks=helper1, labels=y_axis_list_str)
# plt.xlabel('in order')
# plt.ylabel('out order')
# plt.title('order scatter')
# plt.show()
# plt.close()
# print(x_axis)
# print(y_axis)

# plt.scatter(x_index_list, y_axis)
# plt.show()
#
# print(stats.pearsonr(x_index_list, y_axis))
