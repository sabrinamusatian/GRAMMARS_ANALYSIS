from common_util import get_graph, get_grammar
from collections import defaultdict
import time
import sys

def matrix_method(grammar_filename, graph_filename):
    graph = get_graph(graph_filename)
    grammar_rules = get_grammar(grammar_filename)

    # make more comfortable representation of grammar for this task
    grammar_term = set()
    grammar_prod = defaultdict(list)
    for key in grammar_rules:
        for prod in grammar_rules[key]:
            if len(prod) == 2:
                grammar_prod[(prod[0], prod[1])].append(key)
            else:
                grammar_term.add(prod[0])
                grammar_prod[(prod[0],)].append(key)

    size, _ = graph.shape
    mat = [[[] for i in range(size)] for j in range(size)]

    # terminal to non-terminal
    for i in range(size):
        for j in range(size):
            for el in graph[i][j]:
                if el in grammar_term:
                    mat[i][j].extend(grammar_prod[(el,)])

    # Transitive closure
    work = True
    timer = time.time()
    while work:
        work = False
        if ((time.time() - timer) // 5 > 1):
            timer = time.time()
            print("Result for " + grammar_filename + " and "
                  + graph_filename + " is still computing. Please wait")
        for a in range(size):
            for b in range(size):
                for c in range(size):
                    for ab in mat[a][b]:
                        for bc in mat[b][c]:
                            prob_prod = (ab, bc)
                            if prob_prod in grammar_prod:
                                left = grammar_prod[prob_prod]
                                for el in left:
                                    if el not in mat[a][c]:
                                        mat[a][c].append(el)
                                        work = True
    return [(i, lbl, j) for i in range(size) for j in range(size)
            for lbl in mat[i][j]]

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print("Incorrect number of input parameters. Please try to start script like this:"
              "python matrix_method.py grammars/Q1_homsky data/skos.dot (optional)res.txt")
        sys.exit()

    res = '\n'.join(map(str,matrix_method(sys.argv[1], sys.argv[2])))

    if len(sys.argv) == 3:
        print res
    else:
        with open(sys.argv[3], 'w') as f:
            f.write(res)
            f.close()