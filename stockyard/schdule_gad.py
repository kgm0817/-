#!/usr/bin/env python


from solver import GeneticsSolver
import random
import numpy as np
from generator import generator

import pandas as pd
import random
import copy
import matplotlib.pyplot as plt
from scipy import stats
from util import order
from copy import deepcopy

MUTATION_CHANCE = 0.9
CROSS_OVER_RATE = 0.3
POPULATION_LEN = 100
MAX_ITERATION = 10


def genetic(df):
    x_axis, y_axis = order.order(df)
    x_index_list = range(len(x_axis))
    curr_corr, _ = stats.pearsonr(x_index_list, y_axis)
    print('current', 1 - curr_corr)

    chromosome = [i for i in range(len(df))]

    gSolver = GeneticsSolver(chromosome, df, POPULATION_LEN, MUTATION_CHANCE, CROSS_OVER_RATE)
    gSolver.solve(max_iter=MAX_ITERATION)
    print('\n\n====================================================')
    print('Original:')
    print('Found Solution:')
    print(gSolver.best.gene)
    df_copy = deepcopy(df)
    type_list = [df.loc[i]['type'] for i in gSolver.best.gene]
    block_number_list = [df.loc[i]['block_number'] for i in gSolver.best.gene]

    df_copy['type'] = type_list
    df_copy['block_number'] = block_number_list
    return df_copy


if __name__ == "__main__":
    try:
        SEED = 3
        random.seed(SEED)
        np.random.seed(SEED)
        # numpy 옵션
        np.set_printoptions(threshold=np.inf, linewidth=np.inf)

        params = [30, 30, 3, 7, 0, 100, 100]
        flag = [True, True, True, True]

        new_map, weight_map, df = generator(params, flag)
        x_axis, y_axis = order.order(df)
        x_index_list = range(len(x_axis))
        curr_corr, _ = stats.pearsonr(x_index_list, y_axis)
        print('current', curr_corr)

        chromosome = [i for i in range(len(df))]

        gSolver = GeneticsSolver(chromosome, df, POPULATION_LEN, MUTATION_CHANCE, CROSS_OVER_RATE)
        gSolver.solve(max_iter=MAX_ITERATION)

        print('\n\n====================================================')
        print('Original:')
        print('Found Solution:')
        print(gSolver.best.gene)
        # p.apply_chain(gSolver.best.gene, with_display=True)
        # print('Result:')
        # print(p)
    except KeyboardInterrupt:
        pass