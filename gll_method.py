from common_util import *
import time
import sys

class Stack:
    def __init__(self):
        self.states = []
        self.edges = set()

class Gll_class:
    def __init__(self, graph, size, grammar):
        self.popped = defaultdict(list)
        self.work_list = set()
        self.history = set()
        self.stack = Stack()
        self.res = set()
        self.grammar_pos = None
        self.graph_pos = None
        self.stack_pos = None
        self.graph = graph
        self.grammar = grammar
        self.size = size

    # Case 1: same nonterm for graph and grammar
    def same_nonterm(self, grammar_edge, graph_fr, graph_to, graph_lbl):
        new_config = (grammar_edge.to, graph_to, self.stack_pos)
        if new_config not in self.history and new_config not in self.work_list:
            self.work_list.add(new_config)

    # Case 2: nonterm in Out(Grammar)
    def out_nonterm(self, grammar_edge):
        new_stack_node = (grammar_edge.lbl, self.graph_pos)
        nonterm, pos = new_stack_node
        if new_stack_node not in self.stack.states:
            new_stack_edge = (len(self.stack.states), self.stack_pos, grammar_edge.end)
            self.stack.states.append(new_stack_node)
        else:
            new_stack_edge = (self.stack.states.index(new_stack_node), self.stack_pos,
                              grammar_edge.to)
        new_stack_edge_fr, new_stack_edge_to, new_stack_edge_lbl = new_stack_edge
        if new_stack_edge not in self.stack.edges:
            self.stack.edges.add(new_stack_edge)
        # Already considered stack state, needs to be handled separately
        # Because some new configurations may be missed
        if self.stack.states[new_stack_edge_fr] in self.popped:
            for _, fr in self.popped[self.stack.states[new_stack_edge_fr]]:
                new_config = (new_stack_edge_lbl, fr, new_stack_edge_to)
                if new_config not in self.history and new_config not in self.work_list:
                    self.work_list.add(new_config)
                self.res.add((self.graph_pos, nonterm, fr))
        for node in self.grammar.start[grammar_edge.lbl]:
            new_config = (node, self.graph_pos, new_stack_edge_fr)
            if new_config not in self.history and new_config not in self.work_list:
                self.work_list.add(new_config)

    # Case 3: grammar_pos in End(Grammar)
    def grammar_fin_state(self, end):
        stack_el = self.stack.states[self.stack_pos]
        if end == stack_el[0]:
            for edge_fr, edge_to, edge_lbl in self.stack.edges:
                if edge_fr == self.stack_pos:
                    new_config = (edge_lbl, self.graph_pos, edge_to)
                    if new_config not in self.history and new_config not in self.work_list:
                        self.work_list.add(new_config)
            self.res.add((stack_el[1], stack_el[0], self.graph_pos))
            self.popped[stack_el].append((self.grammar_pos, self.graph_pos))

    # main body to execute algorithm
    def run(self, grammar_filename, graph_filename):
        # Add all the initial states
        for key in self.grammar.start:
            for i in range(self.size):
                for pos in self.grammar.start[key]:
                    self.work_list.add((pos, i, i))
                self.stack.states.append((key, i))
        timer = time.time()
        while self.work_list:
            self.grammar_pos, self.graph_pos, self.stack_pos = self.work_list.pop()
            self.history.add((self.grammar_pos, self.graph_pos, self.stack_pos))
            for grammar_edge in self.grammar.edges:
                if grammar_edge.fr == self.grammar_pos:
                    for graph_fr, graph_to, graph_lbl in self.graph:
                        if self.graph_pos == graph_fr and grammar_edge.lbl == graph_lbl:
                            self.same_nonterm(grammar_edge, graph_fr, graph_to, graph_lbl)
                    if grammar_edge.is_non_term:
                        self.out_nonterm(grammar_edge)
            for end in self.grammar.end[self.grammar_pos]:
                self.grammar_fin_state(end)
            if (time.time() - timer) // 5 > 1:
                timer = time.time()
                print("Result for " + grammar_filename + " and "
                      + graph_filename + " is still computing. Please wait")
        return self.res

def gll(grammar_filename, graph_filename):
    graph = (get_graph(graph_filename))
    size = len(graph)
    graph_edges = set()
    for i in range(size):
        for j in range(size):
            for lbl in graph[i][j]:
                graph_edges.add((i, j, lbl))
    grammar = get_grammar_from_graph(grammar_filename)
    gll_class = Gll_class(graph_edges, size, grammar)
    res_set = gll_class.run(grammar_filename, graph_filename)
    return list(res_set)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Incorrect number of input parameters. Please try to start script like this:"
              "python gll_method.py grammars/Q1_gr data/skos.dot (optional)res.txt")
        sys.exit()

    res = '\n'.join(map(str, gll(sys.argv[1], sys.argv[2])))

    if len(sys.argv) == 3:
        print(res)
    else:
        with open(sys.argv[3], 'w') as f:
            f.write(res)
            f.close()