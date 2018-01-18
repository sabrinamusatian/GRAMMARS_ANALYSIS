from common_util import *
from matrix_method import matrix_method
from glr_method import glr
from gll_method import gll
import os

def read_ans(filename):
    with open(filename) as f:
        lines = f.readlines()
        tmp = []
        for line in lines:
            r = line.rstrip('\n')
            pos1, term, pos2 = r.split(',')
            tmp.append((int(pos1), term, int(pos2)))
        return tmp

def print_ans(res, filename):
    fxi = open(filename, 'w')
    for el in res:
        pos1, term, pos2 = el
        fxi.write(str(pos1) + "," + term + "," + str(pos2) + os.linesep)

test_data_gr= [("small1_graph.dot", "small1_gr","small1_ans"),
            ("small2_graph.dot", "small2_gr", "small2_ans"),
            ("small3_graph.dot", "small3_gr", "small3_ans"),
            ("small4_graph.dot", "small4_gr", "small4_ans"),
            ("small5_graph.dot", "small5_gr", "small5_ans"),
            ("small6_graph.dot", "small5_gr", "small6_ans")]
test_data_homsky= [("small1_graph.dot", "small1_homsky","small1_ans"),
            ("small2_graph.dot", "small2_homsky", "small2_ans"),
            ("small3_graph.dot", "small3_homsky", "small3_ans"),
            ("small4_graph.dot", "small4_homsky", "small4_ans"),
            ("small5_graph.dot", "small5_homsky", "small5_ans"),
            ("small6_graph.dot", "small5_homsky", "small6_ans")]

def check_list_eq(res, ans_list):
    if len(res) == len(ans_list):
        for temp in res:
            if not temp in ans_list:
                return False
        for temp in ans_list:
            if not temp in res:
                return False
    else:
        return False
    return True


def test_glr_method(graph_name, grammar_name, ans_file):
    print ("Test for " + grammar_name + " and " + graph_name + " started.")
    res = list(filter(lambda x: x[1] == 'S',
                      glr("./small_tests/" + grammar_name, "./small_tests/" + graph_name)))
    ans_list = read_ans("./small_tests/" + ans_file)
    if not check_list_eq(res, ans_list):
        print (graph_name + " failed")
        return False
    print ("Test for " + grammar_name + " and "  + graph_name + " completed successfully.")
    return True

def test_gll_method(graph_name, grammar_name, ans_file):
    print ("Test for " + grammar_name + " and " + graph_name + " started.")
    res = list(filter(lambda x: x[1] == 'S',
                      gll("./small_tests/" + grammar_name, "./small_tests/" + graph_name)))
    ans_list = read_ans("./small_tests/" + ans_file)
    if not check_list_eq(res, ans_list):
        print (graph_name + " failed")
        return False
    print ("Test for " + grammar_name + " and " + graph_name + " completed successfully.")
    return True

def test_matrix_method(graph_name, grammar_name, ans_file):
    print ("Test for " + grammar_name + "  and " + graph_name + " started.")
    res = list(filter(lambda x: x[1] == 'S',
                      matrix_method("./small_tests/" + grammar_name, "./small_tests/" + graph_name)))
    ans_list = read_ans("./small_tests/" + ans_file)
    if not check_list_eq(res, ans_list):
        print (graph_name + " failed")
        return False
    print ("Test for " + grammar_name + " and "  + graph_name + " completed successfully.")
    return True

def glr_small_tests(test_data):
    print ("Small tests for glr method started")
    for graph, grammar, ans in test_data:
        temp = test_glr_method(graph, grammar, ans)
        if not temp:
            return False
    print ("All small tests for glr method completed successfully.")
    return True

def gll_small_tests(test_data):
    print ("Small tests for gll method started")
    for graph, grammar, ans in test_data:
        temp = test_gll_method(graph, grammar, ans)
        if not temp:
            return False
    print ("All small tests for gll method completed successfully.")
    return True

def matrix_small_tests(test_data):
    print ("Small tests for matrix method started")
    for graph, grammar, ans in test_data:
        temp = test_matrix_method(graph, grammar, ans)
        if not temp:
            return False
    print ("All small tests for matrix method completed successfully.")
    return True

def run_small_tests():
    print("Starting small tests.")
    glr = glr_small_tests(test_data_gr)
    gll = gll_small_tests(test_data_gr)
    matrix = matrix_small_tests(test_data_homsky)
    if (glr and gll and matrix):
        print("All small tests completed successfully.")
        return True
    else:
        print("Some of the small tests failed.")
        return False
if __name__ == '__main__':
    tmp = run_small_tests()