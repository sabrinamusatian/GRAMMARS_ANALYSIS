from common_util import *
import time
import sys

class Stack:
    def __init__(self):
        self.states = []
        self.edges = set()

def get_edges_from_graph(graph):
    graph_edges = set()
    size, _ = graph.shape
    for i in range(size):
        for j in range(size):
            for lbl in graph[i][j]:
                graph_edges.add((i, j, lbl))
    return (graph_edges, size)

def gll(grammar_filename, graph_filename):
    graph, size = get_edges_from_graph(get_graph(graph_filename))
    grammar = get_grammar_from_graph(grammar_filename)
    popped = defaultdict(list)
    work_list = set()
    history = set()
    stack = Stack()
    res = set()

    # Add all the initial states
    for key in grammar.start:
        for i in range(size):
            for pos in grammar.start[key]:
                work_list.add((pos, i, i))
            stack.states.append((key, i))

    timer = time.time()
    while (work_list):
        grammar_pos, graph_pos, stack_pos = work_list.pop()
        history.add((grammar_pos, graph_pos, stack_pos))
        for grammar_edge in grammar.edges:
            # Case 1: same nonterm for graph and grammar
            if grammar_edge.fr == grammar_pos:
                for graph_fr, graph_to, graph_lbl in graph:
                    if graph_pos == graph_fr and grammar_edge.lbl == graph_lbl:
                        new_config = (grammar_edge.to, graph_to, stack_pos)
                        if new_config not in history and new_config not in work_list:
                            work_list.add(new_config)
                # Case 2: nonterm in Out(Grammar)
                if grammar_edge.is_non_term:
                    new_stack_node = (grammar_edge.lbl, graph_pos)
                    nonterm, pos = new_stack_node
                    if new_stack_node not in stack.states:
                        new_stack_edge = (len(stack.states), stack_pos, grammar_edge.end)
                        stack.states.append(new_stack_node)
                    else:
                        new_stack_edge = (stack.states.index(new_stack_node), stack_pos,
                                                     grammar_edge.to)
                    new_stack_edge_fr, new_stack_edge_to, new_stack_edge_lbl = new_stack_edge
                    if new_stack_edge not in stack.edges:
                        stack.edges.add(new_stack_edge)
                    # Already considered stack state, needs to be handled separately
                    # Because some new configurations may be missed
                    if stack.states[new_stack_edge_fr] in popped:
                        for _, fr in popped[stack.states[new_stack_edge_fr]]:
                            new_config = (new_stack_edge_lbl, fr, new_stack_edge_to)
                            if new_config not in history and new_config not in work_list:
                                work_list.add(new_config)
                            res.add((graph_pos, nonterm, fr))
                    for node in grammar.start[grammar_edge.lbl]:
                        new_config = (node, graph_pos, new_stack_edge_fr)
                        if new_config not in history and new_config not in work_list:
                            work_list.add(new_config)
        # Case 3: grammar_pos in End(Grammar)
        for end in grammar.end[grammar_pos]:
            stack_el = stack.states[stack_pos]
            if end == stack_el[0]:
                for edge_fr, edge_to, edge_lbl in stack.edges:
                    if edge_fr == stack_pos:
                        new_config = (edge_lbl, graph_pos, edge_to)
                        if new_config not in history and new_config not in work_list:
                            work_list.add(new_config)
                res.add((stack_el[1], stack_el[0], graph_pos))
                popped[stack_el].append((grammar_pos, graph_pos))

        if ((time.time() - timer) // 5 > 1):
            timer = time.time()
            print("Result for " + grammar_filename + " and "
                  + graph_filename + " is still computing. Please wait")
    return res

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Incorrect number of input parameters. Please try to start script like this:"
              "python gll_method.py grammars/Q1_gr data/skos.dot (optional)res.txt")
        sys.exit()

    res = '\n'.join(map(str, gll(sys.argv[1], sys.argv[2])))

    if len(sys.argv) == 3:
        print res
    else:
        with open(sys.argv[3], 'w') as f:
            f.write(res)
            f.close()