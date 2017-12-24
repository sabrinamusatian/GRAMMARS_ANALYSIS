import numpy as np

import re
from collections import defaultdict

# Graph represented as a matrix, stored in numpy array
def get_graph(filename):
    with open(filename) as f:
        lines = f.readlines()
        size = lines[2].count(";")
        Gr = [[[] for i in range(size)] for i in range(size)]
        rules_re = r"(?P<lr>\d*) -> (?P<rr>\d*).*\"(?P<lbl>\w*)\".*"
        rules = re.compile(rules_re)
        for line in lines[2:]:
            res = rules.match(line)
            if res:
                i = int(res.group('lr'))
                j = int(res.group('rr'))
                label = res.group('lbl')
                Gr[int(i)][int(j)].append(label)
    return np.array(Gr)

# Grammar represented as productions stored in dictionary
def get_grammar(filename):
    gram = defaultdict(list)
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            l, r = line.split(' -> ')
            r = r.rstrip('\n')
            gram[l].append(r.split(' '))
    return gram


def count_res(res):
    return len(list(filter(lambda x: x[1] == 'S', res)))