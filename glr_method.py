from common_util import get_graph, get_grammar
import time
import sys
from itertools import product

def rec_path(grammar, graph, fr, to, non_term, len_str, work):
    for key in grammar:
        # checks if the input prod is in the current non_terminal productions
        if non_term in grammar[key]:
            if key not in graph[fr][to]:
                graph[fr][to].append(key)
                work[0] = True
    if len_str == 0:
        return
    for new_to in filter(lambda k: bool(graph[to][k]), range(len(graph[to]))):
        for el in graph[to][new_to]:
            rec_path(grammar, graph, fr, new_to, non_term + [el], len_str - 1, work)
    return


def glr(grammar_filename, graph_filename):
    graph = get_graph(graph_filename)
    grammar_prod = get_grammar(grammar_filename)
    size, _ = graph.shape
    work = [True]
    max_len = max(len(el) for prod in grammar_prod.values() for el in prod)
    timer = time.time()
    while work[0]:
        work[0] = False
        for i in range(size):
            rec_path(grammar_prod, graph, i, i, [], max_len, work)
            if ((time.time() - timer) // 5 > 1):
                timer = time.time()
                print("Result for " + grammar_filename + " and "
                      + graph_filename + " is still computing. Please wait")

    return [(i, label, j) for i in range(size) for j in range(size)
            for label in graph[i][j] if label in grammar_prod.keys()]

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print("Incorrect number of input parameters. Please try to start script like this:"
              "python glr_method.py grammars/Q1 data/skos.dot (optional)res.txt")
        sys.exit()

    res = '\n'.join(map(str,glr(sys.argv[1], sys.argv[2])))

    if len(sys.argv) == 3:
        print res
    else:
        with open(sys.argv[3], 'w') as f:
            f.write(res)
            f.close()