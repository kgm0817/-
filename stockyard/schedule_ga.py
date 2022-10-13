from generator import generator
from evaluate import evaluate
import pandas as pd
import random
import numpy as np
import copy
import matplotlib.pyplot as plt
from scipy import stats

from util import scheduleutil
from util import order
from method import inout_2quad
from datetime import datetime
from datetime import timedelta
from util import dfs


def quad2(df, new_map, flag, weight_map, index, total_list):
    curr = 0
    insert_cnt = 0
    area = 0
    out_cnt = 0

    while True:
        task = df.loc[curr]
        if task.type == 1:
            insert_cnt, area = inout_2quad.insert(task, new_map, weight_map, insert_cnt, area, df, flag)
        if task.type == 2:
            out_cnt, df = inout_2quad.out(task, new_map, out_cnt, flag, df, curr)
        curr += 1
        if curr == len(df) - 1:
            break

    total_list[0][index].append(insert_cnt)
    total_list[1][index].append(area)
    total_list[2][index].append(out_cnt)


pd.set_option('display.max_rows', 500)

SEED = 3
random.seed(SEED)
np.random.seed(SEED)
# numpy 옵션
np.set_printoptions(threshold=np.inf, linewidth=np.inf)

params = [20, 20, 3, 7, 0, 30, 30]
flag = [True, True, True, True]

new_map, weight_map, df = generator(params, flag)

df_len, _ = df.shape
allow_time = [random.randrange(20, 40) for _ in range(df_len)]

allow_df = copy.deepcopy(df)
x_axis, y_axis = order.order(allow_df)
print(x_axis)
print(y_axis)
# x_index_list = [i for i,j in enumerate(x_axis)]
x_index_list = range(len(x_axis))
curr_corr, _ = stats.pearsonr(x_index_list, y_axis)

allow_df['allow_time'] = allow_time

include_in = scheduleutil.include_or_time(allow_df)

schedule_index_list = [i for i in range(df_len)]


best_df = None
dd = None

# for z in range(3000):
#     check = False
#     dd = None
#     while not check:
#         random_schedule = scheduleutil.init_schedule(include_in)
#         print(random_schedule)
#         check = scheduleutil.check_schedule(random_schedule, include_in, allow_df)
#         dd = random_schedule
#
#     df_copy = copy.deepcopy(df)
#     type_list = [df_copy.loc[i]['type'] for i in dd]
#     block_number_list = [df_copy.loc[i]['block_number'] for i in dd]
#     df_copy['type'] = type_list
#     df_copy['block_number'] = block_number_list
#     x_axis, y_axis = order.order(df_copy)
#     x_index_list = range(len(x_axis))
#     corr, _ = stats.pearsonr(x_index_list, y_axis)
#     print(curr_corr)
#     if curr_corr < corr:
#         curr_corr = corr
#         best_df = df_copy
#
# print(curr_corr)
# print(best_df)

# curr = 0
# insert_cnt = 0
# area = 0
# out_cnt = 0
#
# while True:
#     task = df.loc[curr]
#     if task.type == 1:
#         insert_cnt, area = inout_2quad.insert(task, new_map, weight_map, insert_cnt, area, df, flag)
#     if task.type == 2:
#         out_cnt, df = inout_2quad.out(task, new_map, out_cnt, flag, df, curr)
#     curr += 1
#     if curr == len(df) - 1:
#         break
#
#     print(insert_cnt, out_cnt)

# schedule_in = df[df.type == 1].reset_index(drop=True)
# schedule_out = df[df.type == 2].reset_index(drop=True)
# # print(schedule_in)
#
# include_in = include_time(schedule_in, 30)
# print(include_in)


# 스케줄 복사
df_copy = copy.deepcopy(df)

# 맵 복사
# new_map_copy = copy.deepcopy(new_map)

# x_axis, y_axis = order.order(df_copy)
# print(x_axis)


#plot
# x_axis_list_str = list(map(str, x_axis))
x_axis_list_str = x_axis
x_index_list = [i for i, j in enumerate(x_axis)]
# print(x_index_list)
plt.plot(x_axis_list_str, y_axis, 'ok')
helper = np.arange(len(x_axis_list_str))
# helper1 = np.arange(len(y_axis_list_str))
plt.xticks(ticks=helper, labels=x_axis_list_str)
# plt.yticks(ticks=helper1, labels=y_axis_list_str)
plt.xlabel('in order')
plt.ylabel('out order')
plt.title('order scatter')
plt.show()
plt.close()
print(x_axis)
print(y_axis)

plt.scatter(x_index_list, y_axis)
plt.show()

print(stats.pearsonr(x_index_list, y_axis))
