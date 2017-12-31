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
    epsilons = []
    with open(filename) as f:

        lines = f.readlines()
        for line in lines:
            l, r = line.split(' -> ')
            r = r.rstrip('\n')
            gram[l].append(r.split(' '))
            if r == "eps":
                epsilons.append(l)
    return gram, epsilons

class grammar_edge(object):
    def __init__(self, fr, to, lbl, is_non_term):
        self.fr = fr
        self.to = to
        self.lbl = lbl
        self.is_non_term = is_non_term


class grammar_graph(object):
    def __init__(self, edges, start, end, size):
        self.edges = edges
        self.start = start
        self.end = end
        self.size = size

# Get grammar represented as recursive automata
def get_grammar_from_graph(filename):
    with open(filename) as f:
        start = defaultdict(list)
        edge = re.compile(r"(?P<lr>\d*) -> (?P<rr>\d*).*\"(?P<lbl>[a-zA-Z0-9_]*)\".*")
        start_or_final =re.compile(r"(?P<node>\d*)\[label=\"(?P<lbl>[a-zA-Z0-9_]*)\".*")
        start_reg = re.compile(r".*color=\"green\".*")
        end_reg = re.compile(r".*shape=\"doublecircle\".*")
        lines = f.readlines()
        size = lines[2].count(";")
        grammar = []
        end = [[] for _ in range(size)]
        for line in lines[2:]:
            is_edge = edge.match(line)
            if is_edge :
                grammar.append(grammar_edge(int(is_edge.group('lr')), int(is_edge.group('rr')),
                                            is_edge.group('lbl'), is_edge.group('lbl').isupper()))

            is_start_or_final = start_or_final.match(line)
            if is_start_or_final:
                is_start = start_reg.match(line)
                is_end = end_reg.match(line)
                if is_start:
                    start[is_start_or_final.group('lbl')].append(int(is_start_or_final.group('node')))
                if is_end:
                    end[int(is_start_or_final.group('node'))].append(is_start_or_final.group('lbl'))
        return grammar_graph(grammar, start, end, size)

def count_res(res):
    return len(list(filter(lambda x: x[1] == 'S', res)))