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
import schdule_gad


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

params = [20, 20, 3, 4, 0, 50, 50]
flag = [True, True, True, True]

new_map, weight_map, df = generator(params, flag)
copy_df = copy.deepcopy(df)
copy_map, copy_weight_map = copy.deepcopy(new_map), copy.deepcopy(weight_map)
ga_df = schdule_gad.genetic(df)

# df_copy = [copy.deepcopy(df) for _ in range(len(methods))]

curr = 0
insert_cnt = 0
area = 0
out_cnt = 0
while True:
    task = copy_df.loc[curr]
    if task.type == 1:
        insert_cnt, area = inout_2quad.insert(task, new_map, weight_map, insert_cnt, area, copy_df, flag)
    if task.type == 2:
        out_cnt, copy_df = inout_2quad.out(task, new_map, out_cnt, flag, copy_df, curr)
    curr += 1
    if curr == len(copy_df) - 1:
        break

print(insert_cnt, out_cnt)

curr = 0
insert_cnt = 0
area = 0
out_cnt = 0
while True:
    task = ga_df.loc[curr]
    if task.type == 1:
        insert_cnt, area = inout_2quad.insert(task, copy_map, copy_weight_map, insert_cnt, area, ga_df, flag)
    if task.type == 2:
        out_cnt, ga_df = inout_2quad.out(task, copy_map, out_cnt, flag, ga_df, curr)
    curr += 1
    if curr == len(ga_df) - 1:
        break

print(insert_cnt, out_cnt)