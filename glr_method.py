from common_util import *
import time
import sys
import Queue

def glr(grammar_filename, graph_filename):
    graph = get_graph(graph_filename)
    grammar = get_grammar_from_graph(grammar_filename)
    size_graph, _ = graph.shape
    states = defaultdict(int)
    # creating future states like (grammar_pos, graph_pos)
    states_number = grammar.size * size_graph + 1
    states_init = defaultdict(tuple)
    work = True
    matrix = [[[] for _ in range(states_number)] for _ in range(states_number)]
    itr = 0
    for i in range(grammar.size):
        for j in range(size_graph):
            states[(i, j)] = itr
            states_init[itr] = (i, j)
            itr += 1
    timer = time.time()
    while work:
        work = False
        if (time.time() - timer) // 5 > 1:
            timer = time.time()
            print("Result for " + grammar_filename + " and "
                  + graph_filename + " is still computing. Please wait")
        # adding edges between configuration states
        for fr in range(size_graph):
            for to in range(size_graph):
                for el in graph[fr][to]:
                    for grammar_edge in grammar.edges:
                        if el == grammar_edge.lbl:
                            from_config = states[(grammar_edge.fr, fr)]
                            to_config = states[(grammar_edge.to, to)]
                            if el not in matrix[from_config][to_config]:
                                matrix[from_config][to_config].append(el)
        # finding ways between start and end positions for grammar
        for nonterm in grammar.start:
            for pos in grammar.start[nonterm]:
                for i in range(size_graph):
                    # BFS
                    visited = [False for _ in range(states_number)]
                    queue = Queue.Queue()
                    queue.put(states[(pos, i)])
                    visited[states[(pos, i)]] = True
                    while not queue.empty():
                        front = queue.get()
                        gram_pos, graph_pos = states_init[front]
                        if nonterm in grammar.end[gram_pos] and nonterm not in graph[i][graph_pos]:
                            graph[i][graph_pos].append(nonterm)
                            work = True
                        for next in range(states_number):
                            if not visited[next] and matrix[front][next]:
                                queue.put(next)
                                visited[next] = True

    return list(filter(lambda x: x[1].isupper(), [(i, lbl, j) for i in range(size_graph) for j in range(size_graph)
            for lbl in graph[i][j]]))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Incorrect number of input parameters. Please try to start script like this:"
              "python glr_method.py grammars/Q1_gr data/skos.dot (optional)res.txt")
        sys.exit()

    res = '\n'.join(map(str, glr(sys.argv[1], sys.argv[2])))

    if len(sys.argv) == 3:
        print res
    else:
        with open(sys.argv[3], 'w') as f:
            f.write(res)
            f.close()
