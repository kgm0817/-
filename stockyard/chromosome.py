import random
from copy import deepcopy
from util import order
from scipy import stats


class Chromosome:
    def __init__(self, gene, df):
        if gene is None:
            gene = []

        self.error = None
        self.error_puzzle_cost = None
        self.error_gene_len = None
        self.gene = gene
        self.df = df
        self.update_error()

    def update_error(self):
        df_copy = deepcopy(self.df)
        type_list = [self.df.loc[i]['type'] for i in self.gene]
        block_number_list = [self.df.loc[i]['block_number'] for i in self.gene]

        df_copy['type'] = type_list
        df_copy['block_number'] = block_number_list
        df_list = [[row['type'], row['block_number']] for idx, row in df_copy.iterrows()]

        for i, j in enumerate(df_list):
            for z, k in enumerate(df_list[i + 1:]):
                if j[1] == k[1]:
                    if j[0] == 2:
                        self.gene[i], self.gene[i + z + 1] = self.gene[i + z + 1], self.gene[i]

        type_list = [self.df.loc[i]['type'] for i in self.gene]
        block_number_list = [self.df.loc[i]['block_number'] for i in self.gene]
        df_copy['type'] = type_list
        df_copy['block_number'] = block_number_list

        x_axis, y_axis = order.order(df_copy)
        x_index_list = range(len(x_axis))

        curr_corr, _ = stats.pearsonr(x_index_list, y_axis)

        self.error = 1 - curr_corr

    @staticmethod
    def cross_over(a, b, df):
        if len(b.gene) > len(a.gene):
            return Chromosome.cross_over(b, a, df)

        geneA = []
        geneB = []

        len_a = len(a.gene)
        len_b = len(b.gene)

        for i in range(len_a//2):
            geneA.append(a.gene[i])
            geneB.append(b.gene[i])
        for i in range(len_a//2, len_a):
            geneA.append(b.gene[i])
            geneB.append(a.gene[i])

        avail_list = [i for i in range(len_a)]
        for i in list(set(geneA)):
            avail_list.remove(i)

        change_list = []
        for a, b in enumerate(geneA):
            for c, d in enumerate(geneA[a+1:]):
                if b == d:
                    change_list.append(a+c+1)

        for i in change_list:
            choice_num = random.choice(avail_list)
            avail_list.remove(choice_num)
            geneA[i] = choice_num

        avail_list = [i for i in range(len_a)]
        for i in list(set(geneB)):
            avail_list.remove(i)

        change_list = []
        for a, b in enumerate(geneB):
            for c, d in enumerate(geneB[a + 1:]):
                if b == d:
                    change_list.append(a)

        for i in change_list:
            choice_num = random.choice(avail_list)
            avail_list.remove(choice_num)
            geneB[i] = choice_num

        return Chromosome(gene=geneA, df=df), Chromosome(gene=geneB, df=df)

    def mutate(self, allow_only_growing=False):
        choice1 = random.choice(self.gene)
        choice2 = random.choice(self.gene)
        if choice2 != choice1:
            self.gene[self.gene.index(choice1)], self.gene[self.gene.index(choice2)] = self.gene[self.gene.index(choice2)], self.gene[self.gene.index(choice1)]

    def __str__(self):
        return '(%d)  %s' % (len(self.gene), ' -> '.join(self.gene))